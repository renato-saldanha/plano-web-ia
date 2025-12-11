#!/usr/bin/env python3
"""
API FastAPI com Histórico de Chat - Template (Nível 2)

Preencha os TODOs seguindo GUIA_APRENDIZADO.md e o exemplo_referencia.py.
Objetivo: adicionar sistema de histórico de conversas ao /api/chat,
mantendo contexto entre mensagens.

Uso:
    uvicorn template:app --reload --port 8000

Regras:
- Não usar autocomplete/IA para gerar código.
- Manter tempo total em 160min (ver checklist.md).
"""

import os
import uuid
import bcrypt
from typing import AsyncIterator, Optional, List, Dict, Literal
from datetime import datetime, timedelta, timezone

from fastapi import FastAPI, Depends, HTTPException, Request, status
from fastapi.responses import StreamingResponse
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
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

# =============================================================================
# TODO 1: Carregar variáveis de ambiente (herdado do Dia 3)
# =============================================================================
load_dotenv()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
if not JWT_SECRET_KEY:
    raise Exception("Favor verificar a JWT_SECRET_KEY")

JWT_ALGORITHM = os.getenv("ALGORITHM")
if not JWT_ALGORITHM:
    raise Exception("Favor verificar o JWT_ALGORITHM")

ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
if not ACCESS_TOKEN_EXPIRE_MINUTES:
    raise Exception("Favor verificar o ACCESS_TOKEN_EXPIRE_MINUTES")

REFRESH_TOKEN_EXPIRE_DAYS = os.getenv("REFRESH_TOKEN_EXPIRE_DAYS")
if not REFRESH_TOKEN_EXPIRE_DAYS:
    raise Exception("Favor verificar o REFRESH_TOKEN_EXPIRE_DAYS")

DEFAULT_MODEL = "gpt-4o-mini"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# =============================================================================
# TODO 2: Armazenamento em memória para histórico
# =============================================================================
# Estrutura: {user_id: {conversation_id: [messages]}}
# TODO: Criar dict vazio chamado 'conversations'
conversations: Dict[str, Dict[str, List[Dict]]] = {}

# =============================================================================
# Configurar FastAPI + CORS
# =============================================================================
app = FastAPI(
    title="API com Histórico de Chat",
    description="Dia 4 - Sistema de histórico de conversas",
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
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame_options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        return response

app.add_middleware(SecurityHeadersMiddleware)

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# =============================================================================
# Auth - Reutilizar do Dia 3
# =============================================================================
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def verify_token(token: str, expected_type: str = "access") -> dict:
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        token_type = payload.get("type")
        if token_type != expected_type:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Tipo de token inválido ({token_type})",
            )
        return payload
    except JWTError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Token inválido ou expirado: {exc}",
        ) from exc


async def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    payload = verify_token(token, expected_type="access")
    username = payload.get("sub")
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não autorizado",
        )
    return {"username": username, "payload": payload}


# =============================================================================
# TODO 3: Modelos Pydantic para histórico
# =============================================================================
# TODO: Criar modelo Message com role (Literal["user", "assistant"]), content e timestamp opcional
class Message(BaseModel):
    role: Literal["user", "assistant"]
    content: str
    timestamp: Optional[str] = None


# TODO: Criar modelo ConversationSummary com id, created_at, last_message opcional, message_count
class ConversationSummary(BaseModel):
    id: str
    created_at: str
    last_message: Optional[str] = None
    message_count: int


# Modificar ChatRequest para incluir conversation_id
class ChatRequest(BaseModel):
    message: str = Field(..., description="Mensagem do usuário")
    conversation_id: Optional[str] = Field(None, description="ID da conversa (cria nova se não fornecido)")
    model: Optional[str] = Field(default=None, description="Modelo LLM")
    stream: bool = Field(default=True, description="Se true, responde via SSE")


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class LoginRequest(BaseModel):
    username: str
    password: str


class RefreshRequest(BaseModel):
    refresh_token: str


class GenerateRequest(BaseModel):
    prompt: str
    model: Optional[str] = None


# =============================================================================
# TODO 4: Funções auxiliares de histórico
# =============================================================================
def get_or_create_conversation(user_id: str, conversation_id: Optional[str] = None) -> str:
    """
    Retorna conversation_id existente ou cria novo.
    
    Args:
        user_id: ID do usuário
        conversation_id: ID da conversa (opcional)
    
    Returns:
        str: ID da conversa (existente ou novo)
    
    TODO:
    1. Se user_id não existe em conversations, criar dict vazio
    2. Se conversation_id fornecido e existe, retornar ele
    3. Se não existe ou None, criar novo com uuid.uuid4()
    4. Retornar conversation_id
    """
    # TODO: Implementar
    pass


def add_message(user_id: str, conversation_id: str, role: str, content: str) -> None:
    """
    Adiciona mensagem à conversa.
    
    Args:
        user_id: ID do usuário
        conversation_id: ID da conversa
        role: "user" ou "assistant"
        content: Conteúdo da mensagem
    
    TODO:
    1. Garantir que user_id existe em conversations
    2. Garantir que conversation_id existe
    3. Criar dict com role, content e timestamp (datetime.utcnow().isoformat())
    4. Adicionar à lista de mensagens
    """
    # TODO: Implementar
    pass


def get_messages(user_id: str, conversation_id: str) -> List[Dict]:
    """
    Retorna lista de mensagens de uma conversa.
    
    Args:
        user_id: ID do usuário
        conversation_id: ID da conversa
    
    Returns:
        List[Dict]: Lista de mensagens
    
    TODO:
    1. Verificar se user_id e conversation_id existem
    2. Retornar lista de mensagens (ou [] se não existir)
    """
    # TODO: Implementar
    pass


def list_conversations(user_id: str) -> List[Dict]:
    """
    Lista todas as conversas do usuário.
    
    Args:
        user_id: ID do usuário
    
    Returns:
        List[Dict]: Lista com {id, created_at, last_message, message_count}
    
    TODO:
    1. Buscar conversas do user_id
    2. Para cada conversa, extrair:
       - id: conversation_id
       - created_at: timestamp da primeira mensagem
       - last_message: conteúdo da última mensagem (se houver)
       - message_count: número de mensagens
    3. Retornar lista ordenada por created_at (mais recente primeiro)
    """
    # TODO: Implementar
    pass


# =============================================================================
# Função de streaming (modificada para usar histórico)
# =============================================================================
async def stream_llm(messages: List, model: str) -> AsyncIterator[str]:
    """
    Gera tokens do LLM com contexto de histórico.
    
    Args:
        messages: Lista de HumanMessage/AIMessage (com histórico)
        model: Nome do modelo
    
    TODO:
    1. Instanciar llm = ChatOpenAI(model=model, streaming=True)
    2. Iterar com async for chunk in llm.astream(messages)
    3. Yield f"data: {chunk.content}\\n\\n" (pular vazios)
    4. Yield "data: [DONE]\\n\\n" ao final
    """
    # TODO: Implementar
    pass


# =============================================================================
# Auth endpoints (herdado do Dia 3)
# =============================================================================
FAKE_USER = {
    "username": "admin",
    "hashed_password": pwd_context.hash("admin123"),
}


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    time_utc = datetime.now(timezone.utc)
    time_delta = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    expire = time_utc + time_delta
    to_encode.update({
        "exp": int(expire.timestamp()),
        "type": "access",
    })
    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)


def create_refresh_token(data: dict) -> str:
    to_encode = data.copy()
    time_utc = datetime.now(timezone.utc)
    time_delta = timedelta(days=int(REFRESH_TOKEN_EXPIRE_DAYS))
    expire = time_utc + time_delta
    to_encode.update({
        "exp": int(expire.timestamp()),
        "type": "refresh",
    })
    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)


@app.post("/login", response_model=Token)
@limiter.limit("5/minute")
async def login(request: Request, login_data: LoginRequest):
    if login_data.username != FAKE_USER["username"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário inválido."
        )
    if not pwd_context.verify(login_data.password, FAKE_USER["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Senha inválida."
        )
    access_token = create_access_token(data={"sub": login_data.username})
    refresh_token = create_refresh_token(data={"sub": login_data.username})
    return Token(access_token=access_token, refresh_token=refresh_token)


@app.post("/refresh", response_model=Token)
async def refresh(request: RefreshRequest):
    payload = verify_token(request.refresh_token, expected_type="refresh")
    username = payload.get("sub")
    access_token = create_access_token(data={"sub": username})
    refresh_token = create_refresh_token(data={"sub": username})
    return Token(access_token=access_token, refresh_token=refresh_token)


# =============================================================================
# TODO 5: Modificar endpoint /api/chat para usar histórico
# =============================================================================
@app.post("/chat")
async def chat(
    request: ChatRequest,
    current_user: dict = Depends(get_current_user),
):
    """
    Endpoint de chat com histórico.
    
    TODO:
    1. Obter user_id de current_user["username"]
    2. Obter ou criar conversation_id usando get_or_create_conversation()
    3. Buscar histórico usando get_messages()
    4. Converter histórico para formato LangChain (HumanMessage/AIMessage)
    5. Adicionar nova mensagem do usuário à lista
    6. Se stream=True: usar stream_llm() e retornar StreamingResponse
    7. Se stream=False: chamar llm.ainvoke() e retornar JSON
    8. Salvar ambas mensagens (user + assistant) no histórico usando add_message()
    9. Retornar resposta incluindo conversation_id
    """
    # TODO: Implementar
    model = request.model or DEFAULT_MODEL
    user_id = current_user["username"]
    
    # TODO: Obter/criar conversation_id
    # TODO: Buscar histórico
    # TODO: Construir lista de mensagens
    # TODO: Chamar LLM (stream ou não)
    # TODO: Salvar mensagens no histórico
    # TODO: Retornar resposta
    
    pass


# =============================================================================
# TODO 6: Novo endpoint - Listar conversas
# =============================================================================
@app.get("/conversations", response_model=List[ConversationSummary])
async def list_user_conversations(
    current_user: dict = Depends(get_current_user),
):
    """
    Lista todas as conversas do usuário autenticado.
    
    TODO:
    1. Obter user_id de current_user
    2. Chamar list_conversations(user_id)
    3. Retornar lista formatada como ConversationSummary
    """
    # TODO: Implementar
    pass


# =============================================================================
# TODO 7: Novo endpoint - Obter mensagens de uma conversa
# =============================================================================
@app.get("/conversations/{conversation_id}/messages", response_model=List[Message])
async def get_conversation_messages(
    conversation_id: str,
    current_user: dict = Depends(get_current_user),
):
    """
    Retorna todas as mensagens de uma conversa específica.
    
    TODO:
    1. Obter user_id de current_user
    2. Verificar se conversa pertence ao usuário (segurança!)
    3. Buscar mensagens usando get_messages()
    4. Retornar lista formatada como Message
    5. Se conversa não encontrada, retornar 404
    """
    # TODO: Implementar
    pass


# =============================================================================
# Endpoint /api/generate (mantido do Dia 3, sem histórico)
# =============================================================================
async def stream_llm_simple(prompt: str, model: str) -> AsyncIterator[str]:
    """Versão simples sem histórico (para /api/generate)."""
    llm = ChatOpenAI(model=model, streaming=True, temperature=0.2)
    async for chunk in llm.astream([HumanMessage(content=prompt)]):
        if chunk.content:
            yield f"data: {chunk.content}\n\n"
    yield "data: [DONE]\n\n"


@app.post("/api/generate")
async def generate(
    request: GenerateRequest,
    current_user: dict = Depends(get_current_user),
):
    """Endpoint simples de streaming (sem histórico)."""
    model = request.model or DEFAULT_MODEL
    return StreamingResponse(
        stream_llm_simple(request.prompt, model=model),
        media_type="text/event-stream"
    )


@app.get("/health")
async def health():
    return {"status": "healthy", "feature": "chat_history"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
