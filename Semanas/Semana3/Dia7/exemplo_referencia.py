#!/usr/bin/env python3
"""
API FastAPI com Swagger/OpenAPI e Deploy - Exemplo Completo

Este arquivo contém uma implementação completa e comentada para referência.
Use este arquivo para consultar quando estiver completando o template.py.

Uso:
    uvicorn exemplo_referencia:app --reload --port 8000
"""

import os
import uuid
import json
import time
import logging
from datetime import datetime, timedelta, timezone
from typing import AsyncIterator, Optional, List, Dict, Literal

from fastapi import FastAPI, Depends, HTTPException, Request, status
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from passlib.context import CryptContext
from pydantic import BaseModel, Field
from jose import JWTError, jwt
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.status import HTTP_404_NOT_FOUND

# =============================================================================
# Configuração
# =============================================================================
load_dotenv()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "7"))
DEFAULT_MODEL = "gpt-4o-mini"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Armazenamento em memória
conversations: Dict[str, Dict[str, List[Dict]]] = {}

# =============================================================================
# Logging Estruturado
# =============================================================================
class JSONFormatter(logging.Formatter):
    """Formatter que serializa logs em formato JSON."""
    
    def format(self, record):
        log_data = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }
        
        # Adicionar campos extras se existirem
        if hasattr(record, "user_id"):
            log_data["user_id"] = record.user_id
        if hasattr(record, "conversation_id"):
            log_data["conversation_id"] = record.conversation_id
        if hasattr(record, "method"):
            log_data["method"] = record.method
        if hasattr(record, "path"):
            log_data["path"] = record.path
        if hasattr(record, "status_code"):
            log_data["status_code"] = record.status_code
        if hasattr(record, "duration_ms"):
            log_data["duration_ms"] = record.duration_ms
        
        return json.dumps(log_data)


# Configurar logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)


def log_structured(level: str, message: str, **kwargs):
    """
    Função helper para logging estruturado.
    
    Args:
        level: Nível do log (INFO, WARNING, ERROR, etc.)
        message: Mensagem do log
        **kwargs: Campos extras para incluir no log
    """
    log_data = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "level": level,
        "message": message,
        **kwargs
    }
    
    log_json = json.dumps(log_data)
    
    if level == "ERROR":
        logger.error(log_json)
    elif level == "WARNING":
        logger.warning(log_json)
    else:
        logger.info(log_json)


# =============================================================================
# FastAPI App com Metadados OpenAPI Configurados
# =============================================================================
app = FastAPI(
    title="API FastAPI com IA Generativa",
    description="""
    API REST completa com integração de IA generativa usando LangChain.
    
    ## Funcionalidades
    
    * **Autenticação JWT**: Login e refresh tokens
    * **Chat com IA**: Conversação com histórico usando OpenAI
    * **Rate Limiting**: Proteção contra abuso por usuário
    * **Logging Estruturado**: Logs em formato JSON
    * **Exception Handling**: Tratamento padronizado de erros
    
    ## Documentação
    
    * **Swagger UI**: Disponível em `/docs`
    * **ReDoc**: Disponível em `/redoc`
    """,
    version="1.0.0",
    contact={
        "name": "Seu Nome",
        "email": "seu.email@exemplo.com",
    },
    license_info={
        "name": "MIT",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        
        # Headers modernos de segurança
        response.headers["Content-Security-Policy"] = "default-src 'self'"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Permissions-Policy"] = "geolocation=(), microphone=()"
        
        return response

app.add_middleware(SecurityHeadersMiddleware)


# =============================================================================
# Rate Limiting por Usuário
# =============================================================================
def get_user_id_for_rate_limit(request: Request) -> str:
    """
    Extrai user_id do token JWT para usar como chave de rate limiting.
    Se não houver token, usa IP como fallback.
    """
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return get_remote_address(request)
    
    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        user_id = payload.get("sub")
        return user_id or get_remote_address(request)
    except Exception:
        return get_remote_address(request)


limiter = Limiter(key_func=get_user_id_for_rate_limit)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# =============================================================================
# Exception Handlers Globais
# =============================================================================
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Trata HTTPException retornando JSON padronizado."""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": True,
            "message": exc.detail,
            "status_code": exc.status_code,
            "path": str(request.url.path),
        }
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Trata erros de validação do Pydantic."""
    errors = []
    for error in exc.errors():
        errors.append({
            "field": ".".join(str(loc) for loc in error["loc"]),
            "message": error["msg"],
            "type": error["type"],
        })
    
    return JSONResponse(
        status_code=422,
        content={
            "error": True,
            "message": "Erro de validação",
            "errors": errors,
            "status_code": 422,
            "path": str(request.url.path),
        }
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Trata erros inesperados (catch-all)."""
    # Logar erro completo para debug
    logger.error(
        f"Erro inesperado: {exc}",
        exc_info=True,
        extra={
            "path": str(request.url.path),
            "method": request.method,
        }
    )
    
    # Retornar mensagem genérica ao cliente
    return JSONResponse(
        status_code=500,
        content={
            "error": True,
            "message": "Erro interno do servidor",
            "status_code": 500,
            "path": str(request.url.path),
        }
    )


# =============================================================================
# Middleware de Request Logging
# =============================================================================
class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time
        
        log_structured(
            "INFO",
            "Request processada",
            method=request.method,
            path=str(request.url.path),
            status_code=response.status_code,
            duration_ms=round(duration * 1000, 2),
            client_ip=request.client.host if request.client else None,
        )
        
        return response

app.add_middleware(RequestLoggingMiddleware)


# =============================================================================
# Autenticação
# =============================================================================
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def verify_token(token: str, expected_type: str = "access") -> dict:
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        if payload.get("type") != expected_type:
            raise HTTPException(status_code=401, detail="Tipo de token inválido")
        return payload
    except JWTError as exc:
        raise HTTPException(status_code=401, detail=f"Token inválido: {exc}") from exc


async def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    payload = verify_token(token, expected_type="access")
    username = payload.get("sub")
    if not username:
        raise HTTPException(status_code=401, detail="Usuário não autorizado")
    return {"username": username, "payload": payload}


# =============================================================================
# Modelos Pydantic com Descrições e Exemplos
# =============================================================================
class Message(BaseModel):
    role: Literal["user", "assistant"] = Field(
        ..., description="Papel da mensagem (usuário ou assistente)"
    )
    content: str = Field(..., description="Conteúdo da mensagem")
    timestamp: Optional[str] = Field(
        None, description="Timestamp ISO da mensagem"
    )


class ConversationSummary(BaseModel):
    id: str = Field(..., description="ID único da conversa", example="uuid-here")
    created_at: str = Field(..., description="Data de criação (ISO format)")
    last_message: Optional[str] = Field(
        None, description="Última mensagem da conversa"
    )
    message_count: int = Field(..., description="Número de mensagens na conversa")


class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        description="Mensagem do usuário para a IA",
        example="Explique o que é Python"
    )
    conversation_id: Optional[str] = Field(
        None,
        description="ID da conversa. Se não fornecido, cria nova conversa",
        example="uuid-here"
    )
    model: Optional[str] = Field(
        None,
        description="Modelo LLM a usar (padrão: gpt-4o-mini)",
        example="gpt-4o-mini"
    )
    stream: bool = Field(
        True,
        description="Se true, retorna resposta via Server-Sent Events (SSE)",
        example=True
    )


class Token(BaseModel):
    access_token: str = Field(..., description="Token de acesso JWT")
    refresh_token: str = Field(..., description="Token de refresh JWT")
    token_type: str = Field("bearer", description="Tipo do token")


class LoginRequest(BaseModel):
    username: str = Field(..., description="Nome de usuário", example="admin")
    password: str = Field(..., description="Senha do usuário", example="admin123")


class RefreshRequest(BaseModel):
    refresh_token: str = Field(..., description="Token de refresh para renovar acesso")


class GenerateRequest(BaseModel):
    prompt: str = Field(..., description="Prompt para geração de texto")
    model: Optional[str] = Field(None, description="Modelo LLM a usar")


# =============================================================================
# Funções de Histórico
# =============================================================================
def get_or_create_conversation(user_id: str, conversation_id: Optional[str] = None) -> str:
    if user_id not in conversations:
        conversations[user_id] = {}
    if conversation_id and conversation_id in conversations[user_id]:
        return conversation_id
    new_id = str(uuid.uuid4())
    conversations[user_id][new_id] = []
    return new_id


def add_message(user_id: str, conversation_id: str, role: str, content: str) -> None:
    if user_id not in conversations:
        conversations[user_id] = {}
    if conversation_id not in conversations[user_id]:
        conversations[user_id][conversation_id] = []
    message = {
        "role": role,
        "content": content,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    conversations[user_id][conversation_id].append(message)


def get_messages(user_id: str, conversation_id: str) -> List[Dict]:
    if user_id not in conversations:
        return []
    if conversation_id not in conversations[user_id]:
        return []
    return conversations[user_id][conversation_id].copy()


def list_conversations(user_id: str) -> List[Dict]:
    if user_id not in conversations:
        return []
    result = []
    for conv_id, messages in conversations[user_id].items():
        if not messages:
            continue
        created_at = messages[0].get("timestamp", datetime.now(timezone.utc).isoformat())
        last_msg = messages[-1].get("content", "") if messages else None
        result.append({
            "id": conv_id,
            "created_at": created_at,
            "last_message": last_msg,
            "message_count": len(messages)
        })
    result.sort(key=lambda x: x["created_at"], reverse=True)
    return result


# =============================================================================
# Endpoints de Autenticação
# =============================================================================
FAKE_USER = {
    "username": "admin",
    "hashed_password": pwd_context.hash("admin123"),
}


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": int(expire.timestamp()), "type": "access"})
    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)


def create_refresh_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": int(expire.timestamp()), "type": "refresh"})
    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)


@app.post("/login", response_model=Token, tags=["Auth"])
@limiter.limit("5/minute")
async def login(request: Request, login_data: LoginRequest):
    """
    Endpoint de autenticação.
    
    Retorna tokens de acesso e refresh após validar credenciais.
    
    - **username**: Nome de usuário (padrão: admin)
    - **password**: Senha do usuário (padrão: admin123)
    
    Rate limit: 5 requisições por minuto por IP/usuário.
    """
    if login_data.username != FAKE_USER["username"]:
        raise HTTPException(status_code=401, detail="Usuário inválido")
    if not pwd_context.verify(login_data.password, FAKE_USER["hashed_password"]):
        raise HTTPException(status_code=401, detail="Senha inválida")
    
    access_token = create_access_token(data={"sub": login_data.username})
    refresh_token = create_refresh_token(data={"sub": login_data.username})
    
    log_structured("INFO", "Login bem-sucedido", user_id=login_data.username)
    
    return Token(access_token=access_token, refresh_token=refresh_token)


@app.post("/refresh", response_model=Token, tags=["Auth"])
async def refresh(request: RefreshRequest):
    """
    Endpoint para renovar tokens de acesso.
    
    Usa o refresh token para gerar novos tokens de acesso e refresh.
    
    - **refresh_token**: Token de refresh válido
    """
    payload = verify_token(request.refresh_token, expected_type="refresh")
    username = payload.get("sub")
    access_token = create_access_token(data={"sub": username})
    refresh_token = create_refresh_token(data={"sub": username})
    return Token(access_token=access_token, refresh_token=refresh_token)


# =============================================================================
# Endpoint /chat com Rate Limiting
# =============================================================================
@app.post("/chat", tags=["Chat"])
@limiter.limit("30/minute")
async def chat(
    request: Request,
    chat_request: ChatRequest,
    current_user: dict = Depends(get_current_user),
):
    """
    Endpoint de chat com histórico e IA generativa.
    
    Processa mensagem do usuário e retorna resposta da IA, mantendo contexto da conversa.
    
    - **message**: Mensagem do usuário
    - **conversation_id**: ID da conversa (opcional, cria nova se não fornecido)
    - **model**: Modelo LLM a usar (opcional, padrão: gpt-4o-mini)
    - **stream**: Se true, retorna resposta via SSE (padrão: true)
    
    Rate limit: 30 requisições por minuto por usuário.
    
    Requer autenticação: Bearer token no header Authorization.
    """
    user_id = current_user["username"]
    model = chat_request.model or DEFAULT_MODEL
    
    conversation_id = get_or_create_conversation(user_id, chat_request.conversation_id)
    
    log_structured(
        "INFO",
        "Início de chat",
        user_id=user_id,
        conversation_id=conversation_id,
        model=model
    )
    
    try:
        stored_messages = get_messages(user_id, conversation_id)
        
        langchain_messages = []
        for msg in stored_messages:
            if msg["role"] == "user":
                langchain_messages.append(HumanMessage(content=msg["content"]))
            elif msg["role"] == "assistant":
                langchain_messages.append(AIMessage(content=msg["content"]))
        
        langchain_messages.append(HumanMessage(content=chat_request.message))
        add_message(user_id, conversation_id, "user", chat_request.message)
        
        if chat_request.stream:
            async def generate():
                llm = ChatOpenAI(model=model, streaming=True, temperature=0.2)
                full_response = ""
                
                async for chunk in llm.astream(langchain_messages):
                    if chunk.content:
                        full_response += chunk.content
                        yield f"data: {chunk.content}\n\n"
                
                yield "data: [DONE]\n\n"
                add_message(user_id, conversation_id, "assistant", full_response)
            
            return StreamingResponse(generate(), media_type="text/event-stream")
        else:
            llm = ChatOpenAI(model=model, temperature=0.2)
            ai_response = await llm.ainvoke(langchain_messages)
            response_content = ai_response.content
            add_message(user_id, conversation_id, "assistant", response_content)
            
            return {
                "reply": response_content,
                "conversation_id": conversation_id,
                "user": user_id,
                "model": model,
            }
    except Exception as exc:
        log_structured(
            "ERROR",
            "Erro ao processar chat",
            user_id=user_id,
            conversation_id=conversation_id,
            error=str(exc)
        )
        raise


# =============================================================================
# Endpoints de Histórico
# =============================================================================
@app.get("/conversations", response_model=List[ConversationSummary], tags=["Chat"])
async def list_user_conversations(
    current_user: dict = Depends(get_current_user),
):
    """
    Lista todas as conversas do usuário autenticado.
    
    Retorna resumo de cada conversa (ID, data de criação, última mensagem, contagem).
    
    Requer autenticação: Bearer token no header Authorization.
    """
    user_id = current_user["username"]
    convs = list_conversations(user_id)
    return [
        ConversationSummary(
            id=conv["id"],
            created_at=conv["created_at"],
            last_message=conv["last_message"],
            message_count=conv["message_count"]
        )
        for conv in convs
    ]


@app.get("/conversations/{conversation_id}/messages", response_model=List[Message], tags=["Chat"])
async def get_conversation_messages(
    conversation_id: str,
    current_user: dict = Depends(get_current_user),
):
    """
    Retorna todas as mensagens de uma conversa específica.
    
    - **conversation_id**: ID da conversa a recuperar
    
    Requer autenticação: Bearer token no header Authorization.
    """
    user_id = current_user["username"]
    if user_id not in conversations:
        raise HTTPException(status_code=404, detail="Conversa não encontrada")
    if conversation_id not in conversations[user_id]:
        raise HTTPException(status_code=404, detail="Conversa não encontrada")
    
    messages = get_messages(user_id, conversation_id)
    return [
        Message(
            role=msg["role"],
            content=msg["content"],
            timestamp=msg.get("timestamp")
        )
        for msg in messages
    ]


@app.post("/api/generate", tags=["Chat"])
async def generate(
    request: GenerateRequest,
    current_user: dict = Depends(get_current_user),
):
    """
    Endpoint simples de geração de texto (sem histórico).
    
    Gera resposta da IA para um prompt único, sem manter contexto.
    
    - **prompt**: Prompt para geração
    - **model**: Modelo LLM a usar (opcional)
    
    Requer autenticação: Bearer token no header Authorization.
    """
    model = request.model or DEFAULT_MODEL
    llm = ChatOpenAI(model=model, streaming=True, temperature=0.2)
    
    async def generate_stream():
        async for chunk in llm.astream([HumanMessage(content=request.prompt)]):
            if chunk.content:
                yield f"data: {chunk.content}\n\n"
        yield "data: [DONE]\n\n"
    
    return StreamingResponse(
        generate_stream(),
        media_type="text/event-stream"
    )


@app.get("/health", tags=["Health"])
async def health():
    """
    Health check endpoint.
    
    Retorna status da API. Usado para monitoramento e load balancers.
    
    Sempre retorna 200 OK se a API está funcionando.
    """
    return {"status": "healthy", "feature": "rate_limiting_logging"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

