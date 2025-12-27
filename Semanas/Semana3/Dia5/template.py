#!/usr/bin/env python3
"""
API FastAPI com Rate Limiting e Logging - Template (Nível 1)

Preencha os TODOs seguindo GUIA_PASSO_A_PASSO.md e o exemplo_completo.py.
Objetivo: adicionar rate limiting por usuário e logging estruturado à API de chat.

Uso:
    uvicorn template:app --reload --port 8000

Regras:
- Não usar autocomplete/IA para gerar código.
- Manter tempo total em 160min (ver checklist.md).
- Usar módulos compartilhados de common/ para reduzir duplicação.
"""

import os
import time
import sys
from pathlib import Path

from dotenv import load_dotenv

# Adicionar diretório pai ao path para importar common
sys.path.insert(0, str(Path(__file__).parent.parent))

# Importar módulos compartilhados
from common.logging import log_structured, setup_logger
from common.auth import get_current_user, create_access_token, create_refresh_token, verify_token
from common.models import ChatRequest, Token, LoginRequest, RefreshRequest, ConversationSummary, Message
from common.conversations import (
    get_or_create_conversation,
    add_message,
    get_messages,
    list_conversations,
    conversations,
)

# LangChain
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

# Rate Limiter
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

# FastAPI
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

# Middleware
from starlette.middleware.base import BaseHTTPMiddleware

# JWT
from jose import jwt

# Hashing
from passlib.context import CryptContext

load_dotenv()

# =============================================================================
# Configuração
# =============================================================================
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
if not JWT_SECRET_KEY:
    raise Exception("Favor verificar a JWT_SECRET_KEY")

JWT_ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "7"))
DEFAULT_MODEL = "gpt-4o-mini"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Configurar logger usando módulo compartilhado
logger = setup_logger(__name__)

# =============================================================================
# FastAPI App
# =============================================================================
app = FastAPI(
    title="API com Rate Limiting e Logging",
    description="Dia 5 - Rate limiting por usuário e logging estruturado",
    version="1.0.0",
)

ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """Middleware que adiciona headers de segurança."""
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        return response

app.add_middleware(SecurityHeadersMiddleware)


# =============================================================================
# TODO 1: Rate Limiting por Usuário
# =============================================================================
# TODO 1.1: Criar função get_user_id_for_rate_limit(request: Request) -> str
# TODO 1.2: Função deve:
#           - Extrair token do header Authorization (Bearer <token>)
#           - Decodificar token JWT usando JWT_SECRET_KEY e JWT_ALGORITHM
#           - Extrair user_id do payload (campo "sub")
#           - Retornar user_id se existir, senão usar get_remote_address(request) como fallback
#           - Tratar exceções e usar IP como fallback em caso de erro
# TODO 1.3: Configurar limiter com key_func=get_user_id_for_rate_limit
# TODO 1.4: Registrar exception handler para RateLimitExceeded
# Dica: Consulte GUIA_PASSO_A_PASSO.md seção 4 e exemplo_completo.py


def get_user_id_for_rate_limit(request: Request) -> str:
    """
    Extrai user_id do token JWT para usar como chave de rate limiting.
    Se não houver token, usa IP como fallback.
    """
    # TODO: Implementar função
    # 1. Extrair header Authorization
    # 2. Verificar se começa com "Bearer "
    # 3. Extrair token
    # 4. Decodificar JWT
    # 5. Extrair user_id (campo "sub")
    # 6. Retornar user_id ou IP como fallback
    
    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Bearer "):
        return get_remote_address(request)

    token = auth_header.split(" ")[1]

    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        user_id = payload.get("sub")
        return user_id or get_remote_address(request)
    except Exception as e:
        return get_remote_address(request)


# Configurar limiter
# TODO: Criar limiter com key_func=get_user_id_for_rate_limit
# limiter = Limiter(key_func=...)
# app.state.limiter = limiter
# app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

limiter = Limiter(key_func=get_user_id_for_rate_limit)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# =============================================================================
# TODO 2: Middleware de Request Logging
# =============================================================================
# TODO 2.1: Criar classe RequestLoggingMiddleware(BaseHTTPMiddleware)
# TODO 2.2: No método dispatch():
#           - Capturar tempo inicial com time.time()
#           - Chamar call_next(request) e aguardar resposta
#           - Calcular duração (tempo_final - tempo_inicial)
#           - Usar log_structured() para logar:
#             * method (request.method)
#             * path (str(request.url.path))
#             * status_code (response.status_code)
#             * duration_ms (duração em milissegundos, arredondado)
#             * client_ip (request.client.host se existir)
# TODO 2.3: Registrar middleware na aplicação
# Dica: Consulte GUIA_PASSO_A_PASSO.md seção 6 e exemplo_completo.py


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """Middleware que loga todas as requisições em formato estruturado."""
    
    async def dispatch(self, request: Request, call_next):
        # TODO: Implementar middleware
        # 1. Capturar tempo inicial
        # 2. Processar requisição (call_next)
        # 3. Calcular duração
        # 4. Logar usando log_structured()
        # 5. Retornar response
        
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
            client_ip=request.client.host if request.client else None
        )
        return response


# TODO: Registrar middleware
# app.add_middleware(RequestLoggingMiddleware)
app.add_middleware(RequestLoggingMiddleware)


# =============================================================================
# Endpoints de Autenticação
# =============================================================================
FAKE_USER = {
    "username": "admin",
    "hashed_password": pwd_context.hash("admin123"),
}


@app.post("/login", response_model=Token)
# TODO: Aplicar rate limit de 5 requisições por minuto
@limiter.limit("5/minute")
async def login(request: Request, login_data: LoginRequest):
    """Endpoint de login que retorna tokens JWT."""
    if login_data.username != FAKE_USER["username"]:
        raise HTTPException(status_code=401, detail="Usuário inválido")
    if not pwd_context.verify(login_data.password, FAKE_USER["hashed_password"]):
        raise HTTPException(status_code=401, detail="Senha inválida")
    
    access_token = create_access_token(data={"sub": login_data.username})
    refresh_token = create_refresh_token(data={"sub": login_data.username})
    
    # TODO: Logar login bem-sucedido usando log_structured()
    # log_structured("INFO", "Login bem-sucedido", user_id=login_data.username)
    log_structured(
        "INFO",
        "Login bem-sucedido",
        user_id=login_data.username
    )
    
    return Token(access_token=access_token, refresh_token=refresh_token)


@app.post("/refresh", response_model=Token)
async def refresh(request: RefreshRequest):
    """Endpoint para renovar tokens usando refresh token."""
    payload = verify_token(request.refresh_token, expected_type="refresh")
    username = payload.get("sub")
    access_token = create_access_token(data={"sub": username})
    refresh_token = create_refresh_token(data={"sub": username})
    return Token(access_token=access_token, refresh_token=refresh_token)


# =============================================================================
# Endpoint /chat com Rate Limiting
# =============================================================================
@app.post("/chat")
# TODO: Aplicar rate limit de 30 requisições por minuto por usuário
@limiter.limit("30/minute")
async def chat(
    request: Request,
    chat_request: ChatRequest,
    current_user: dict = Depends(get_current_user),
):
    """
    Endpoint de chat com histórico e rate limiting por usuário.
    
    Rate limit: 30 requisições por minuto por usuário autenticado.
    """
    user_id = current_user["username"]
    model = chat_request.model or DEFAULT_MODEL
    
    conversation_id = get_or_create_conversation(user_id, chat_request.conversation_id)
    
    # TODO: Logar início de chat usando log_structured()
    # log_structured("INFO", "Início de chat", user_id=user_id, conversation_id=conversation_id, model=model)
    log_structured(
        "INFO", 
        "Inicio de chat", 
        user_id=user_id,
        consversation_id=conversation_id,
        model=model,
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
        # TODO: Logar erro usando log_structured()
        
        log_structured(
            "ERROR", 
            "Erro ao processar chat",
            user_id=user_id,
            conversation_id=conversation_id,
            error=str(exc),
        )
        raise


# =============================================================================
# Endpoints de Histórico
# =============================================================================
@app.get("/conversations")
async def list_user_conversations(
    current_user: dict = Depends(get_current_user),
):
    """Lista todas as conversas do usuário."""
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


@app.get("/conversations/{conversation_id}/messages")
async def get_conversation_messages(
    conversation_id: str,
    current_user: dict = Depends(get_current_user),
):
    """Retorna todas as mensagens de uma conversa."""
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


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy", "feature": "rate_limiting_logging"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
