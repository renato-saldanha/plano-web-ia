#!/usr/bin/env python3
"""
API FastAPI com Histórico de Chat - Exemplo de Referência (Completo)

Este arquivo contém uma implementação completa e comentada para referência.
Use este arquivo para consultar quando estiver completando o template.py.

Uso:
    uvicorn exemplo_referencia:app --reload --port 8000
"""

import os
import uuid
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
# Configuração
# =============================================================================
load_dotenv()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "7"))
DEFAULT_MODEL = "gpt-4o-mini"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# =============================================================================
# Armazenamento em memória
# =============================================================================
# Estrutura: {user_id: {conversation_id: [messages]}}
conversations: Dict[str, Dict[str, List[Dict]]] = {}


# =============================================================================
# FastAPI App
# =============================================================================
app = FastAPI(
    title="API com Histórico de Chat - Referência",
    description="Dia 4 - Exemplo completo",
    version="1.0.0",
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
        response.headers["X-Frame_options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        return response

app.add_middleware(SecurityHeadersMiddleware)

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

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
# Modelos Pydantic
# =============================================================================
class Message(BaseModel):
    role: Literal["user", "assistant"]
    content: str
    timestamp: Optional[str] = None


class ConversationSummary(BaseModel):
    id: str
    created_at: str
    last_message: Optional[str] = None
    message_count: int


class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[str] = None
    model: Optional[str] = None
    stream: bool = True


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class LoginRequest(BaseModel):
    username: str
    password: str


class RefreshRequest(BaseModel):
    refresh_token: str


# =============================================================================
# Funções de Histórico
# =============================================================================
def get_or_create_conversation(user_id: str, conversation_id: Optional[str] = None) -> str:
    """
    Retorna conversation_id existente ou cria novo.
    """
    # Garantir que user_id existe
    if user_id not in conversations:
        conversations[user_id] = {}
    
    # Se conversation_id fornecido e existe, retornar
    if conversation_id and conversation_id in conversations[user_id]:
        return conversation_id
    
    # Criar novo
    new_id = str(uuid.uuid4())
    conversations[user_id][new_id] = []
    return new_id


def add_message(user_id: str, conversation_id: str, role: str, content: str) -> None:
    """Adiciona mensagem à conversa."""
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
    """Retorna lista de mensagens de uma conversa."""
    if user_id not in conversations:
        return []
    if conversation_id not in conversations[user_id]:
        return []
    return conversations[user_id][conversation_id].copy()


def list_conversations(user_id: str) -> List[Dict]:
    """Lista todas as conversas do usuário."""
    if user_id not in conversations:
        return []
    
    result = []
    for conv_id, messages in conversations[user_id].items():
        if not messages:
            continue
        
        # Primeira mensagem (created_at)
        created_at = messages[0].get("timestamp", datetime.now(timezone.utc).isoformat())
        
        # Última mensagem
        last_msg = messages[-1].get("content", "") if messages else None
        
        result.append({
            "id": conv_id,
            "created_at": created_at,
            "last_message": last_msg,
            "message_count": len(messages)
        })
    
    # Ordenar por created_at (mais recente primeiro)
    result.sort(key=lambda x: x["created_at"], reverse=True)
    return result


# =============================================================================
# Função de Streaming com Histórico
# =============================================================================
async def stream_llm(messages: List, model: str) -> AsyncIterator[str]:
    """Gera tokens do LLM com contexto de histórico."""
    llm = ChatOpenAI(model=model, streaming=True, temperature=0.2)
    
    async for chunk in llm.astream(messages):
        if chunk.content:
            yield f"data: {chunk.content}\n\n"
    
    yield "data: [DONE]\n\n"


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


@app.post("/login", response_model=Token)
@limiter.limit("5/minute")
async def login(request: Request, login_data: LoginRequest):
    if login_data.username != FAKE_USER["username"]:
        raise HTTPException(status_code=401, detail="Usuário inválido")
    if not pwd_context.verify(login_data.password, FAKE_USER["hashed_password"]):
        raise HTTPException(status_code=401, detail="Senha inválida")
    
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
# Endpoint /chat com Histórico
# =============================================================================
@app.post("/chat")
async def chat(
    request: ChatRequest,
    current_user: dict = Depends(get_current_user),
):
    """Endpoint de chat com histórico."""
    user_id = current_user["username"]
    model = request.model or DEFAULT_MODEL
    
    # Obter ou criar conversa
    conversation_id = get_or_create_conversation(user_id, request.conversation_id)
    
    # Buscar histórico
    stored_messages = get_messages(user_id, conversation_id)
    
    # Converter para formato LangChain
    langchain_messages = []
    for msg in stored_messages:
        if msg["role"] == "user":
            langchain_messages.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            langchain_messages.append(AIMessage(content=msg["content"]))
    
    # Adicionar nova mensagem do usuário
    langchain_messages.append(HumanMessage(content=request.message))
    
    # Salvar mensagem do usuário
    add_message(user_id, conversation_id, "user", request.message)
    
    # Chamar LLM
    if request.stream:
        # Streaming
        async def generate():
            llm = ChatOpenAI(model=model, streaming=True, temperature=0.2)
            full_response = ""
            
            async for chunk in llm.astream(langchain_messages):
                if chunk.content:
                    full_response += chunk.content
                    yield f"data: {chunk.content}\n\n"
            
            yield "data: [DONE]\n\n"
            
            # Salvar resposta completa após streaming
            add_message(user_id, conversation_id, "assistant", full_response)
        
        return StreamingResponse(generate(), media_type="text/event-stream")
    else:
        # Não-streaming
        llm = ChatOpenAI(model=model, temperature=0.2)
        ai_response = await llm.ainvoke(langchain_messages)
        response_content = ai_response.content
        
        # Salvar resposta
        add_message(user_id, conversation_id, "assistant", response_content)
        
        return {
            "reply": response_content,
            "conversation_id": conversation_id,
            "user": user_id,
            "model": model,
        }


# =============================================================================
# Endpoint: Listar Conversas
# =============================================================================
@app.get("/conversations", response_model=List[ConversationSummary])
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


# =============================================================================
# Endpoint: Obter Mensagens
# =============================================================================
@app.get("/conversations/{conversation_id}/messages", response_model=List[Message])
async def get_conversation_messages(
    conversation_id: str,
    current_user: dict = Depends(get_current_user),
):
    """Retorna todas as mensagens de uma conversa."""
    user_id = current_user["username"]
    
    # Segurança: verificar se conversa pertence ao usuário
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
    return {"status": "healthy", "feature": "chat_history"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
