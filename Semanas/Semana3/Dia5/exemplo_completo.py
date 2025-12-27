#!/usr/bin/env python3
"""
API FastAPI com Rate Limiting e Logging - Exemplo Completo (Nível 1)

Este arquivo contém uma implementação completa e comentada para referência.
Use este arquivo para consultar quando estiver completando o template.py.

Uso:
    uvicorn exemplo_completo:app --reload --port 8000

Notas:
- Este exemplo foca em Rate Limiting por usuário e Logging estruturado
- Exception Handling será abordado no Dia 6
- Usa módulos compartilhados de common/ para reduzir duplicação
"""

import os
import time
from typing import AsyncIterator, Optional

from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from starlette.middleware.base import BaseHTTPMiddleware
from dotenv import load_dotenv

# Importar módulos compartilhados
import sys
from pathlib import Path
# Adicionar diretório pai ao path para importar common
sys.path.insert(0, str(Path(__file__).parent.parent))
from common.logging import JSONFormatter, log_structured, setup_logger
from common.auth import get_current_user, create_access_token, create_refresh_token, verify_token
from common.models import ChatRequest, Token, LoginRequest, RefreshRequest, ConversationSummary, Message
from common.conversations import (
    get_or_create_conversation,
    add_message,
    get_messages,
    list_conversations,
    conversations,
)

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from passlib.context import CryptContext
from jose import jwt

# =============================================================================
# Configuração
# =============================================================================
load_dotenv()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost"],
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
# Rate Limiting por Usuário
# =============================================================================
def get_user_id_for_rate_limit(request: Request) -> str:
    """
    Extrai user_id do token JWT para usar como chave de rate limiting.
    Se não houver token, usa IP como fallback.
    
    Esta função é chamada pelo slowapi para determinar qual chave usar
    para rastrear rate limits. Se o usuário estiver autenticado, usa o
    user_id do token. Caso contrário, usa o IP do cliente.
    
    Args:
        request: Objeto Request do FastAPI
        
    Returns:
        str: user_id (se autenticado) ou IP do cliente (fallback)
    """
    # Tentar extrair token do header Authorization
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        # Se não houver token, usar IP como fallback
        return get_remote_address(request)
    
    # Extrair token do header
    token = auth_header.split(" ")[1]
    
    try:
        # Decodificar token JWT
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        user_id = payload.get("sub")
        # Retornar user_id se existir, senão usar IP
        return user_id or get_remote_address(request)
    except Exception:
        # Se houver erro ao decodificar, usar IP como fallback
        return get_remote_address(request)


# Configurar limiter com função customizada
limiter = Limiter(key_func=get_user_id_for_rate_limit)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# =============================================================================
# Middleware de Request Logging
# =============================================================================
class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware que loga todas as requisições em formato estruturado.
    
    Este middleware captura informações sobre cada requisição:
    - Método HTTP (GET, POST, etc.)
    - Path da requisição
    - Status code da resposta
    - Tempo de processamento em milissegundos
    - IP do cliente
    """
    async def dispatch(self, request: Request, call_next):
        # Capturar tempo inicial
        start_time = time.time()
        
        # Processar requisição
        response = await call_next(request)
        
        # Calcular duração
        duration = time.time() - start_time
        
        # Logar usando função compartilhada
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
# Endpoints de Autenticação
# =============================================================================
FAKE_USER = {
    "username": "admin",
    "hashed_password": pwd_context.hash("admin123"),
}


@app.post("/login", response_model=Token)
@limiter.limit("5/minute")  # Rate limit no login: 5 tentativas por minuto
async def login(request: Request, login_data: LoginRequest):
    """
    Endpoint de login que retorna tokens JWT.
    
    Credenciais de teste:
    - username: admin
    - password: admin123
    
    Rate limit: 5 tentativas por minuto (por IP ou usuário)
    """
    if login_data.username != FAKE_USER["username"]:
        raise HTTPException(status_code=401, detail="Usuário inválido")
    if not pwd_context.verify(login_data.password, FAKE_USER["hashed_password"]):
        raise HTTPException(status_code=401, detail="Senha inválida")
    
    access_token = create_access_token(data={"sub": login_data.username})
    refresh_token = create_refresh_token(data={"sub": login_data.username})
    
    # Logar login bem-sucedido
    log_structured("INFO", "Login bem-sucedido", user_id=login_data.username)
    
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
@limiter.limit("30/minute")  # Rate limit: 30 requisições por minuto por usuário
async def chat(
    request: Request,
    chat_request: ChatRequest,
    current_user: dict = Depends(get_current_user),
):
    """
    Endpoint de chat com histórico e rate limiting por usuário.
    
    Rate limit: 30 requisições por minuto por usuário autenticado.
    Se o usuário exceder o limite, receberá erro 429 (Too Many Requests).
    """
    user_id = current_user["username"]
    model = chat_request.model or DEFAULT_MODEL
    
    conversation_id = get_or_create_conversation(user_id, chat_request.conversation_id)
    
    # Logar início de chat
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
        # Logar erro
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

