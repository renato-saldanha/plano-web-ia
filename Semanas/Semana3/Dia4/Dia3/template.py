#!/usr/bin/env python3
"""
API FastAPI com Streaming (SSE) + LLM - Template (Nível 2)

Preencha os TODOs seguindo GUIA_APRENDIZADO.md e o exemplo_referencia.py.
Objetivo: expor /api/generate com SSE e /chat com streaming opcional,
protegidos por JWT herdado do Dia 2.

Uso:
    uvicorn template:app --reload --port 8000

Regras:
- Não usar autocomplete/IA para gerar código.
- Manter tempo total em 160min (ver checklist.md).
"""

import datetime
import os
from time import timezone
import bcrypt
import re

from typing import AsyncIterator, Optional
from fastapi import FastAPI, Depends, HTTPException, Request, status
from fastapi.responses import StreamingResponse
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from langchain_groq import ChatGroq
from passlib.context import CryptContext
from pydantic import BaseModel, Field
from jose import JWTError, jwt
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from starlette.middleware.base import BaseHTTPMiddleware
# from Semanas.Semana3.Dia2.template import is_token_blacklisted, blacklist_token, 


# =============================================================================
# TODO 1: Carregar variáveis de ambiente
# =============================================================================
# - JWT_SECRET_KEY, JWT_ALGORITHM
# - ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_DAYS (herdar do Dia 2)
# - OPENAI_API_KEY (ou GROQ_API_KEY / ANTHROPIC_API_KEY se trocar provider)
# Dica: use load_dotenv() e os.getenv().
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


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)

class Token(BaseModel):
    access_token: str = Field(description="Token de acesso")
    refresh_token: str = Field(description="Token de atualização")
    token_type: str = Field(description="Tipo de token", default="bearer")

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """
    Classe que define um middleware que adiciona headers de segurança
    """

    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame_options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        return response


# =============================================================================
# TODO 2: Configurar FastAPI + CORS
# =============================================================================
app = FastAPI(
    title="API com Streaming SSE + LLM",
    description="Dia 3 - StreamingResponse + LangChain/LangGraph",
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
app.add_middleware(SecurityHeadersMiddleware)

# Configuração de Rate Limiter básico
limiter = Limiter(key_func = get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# =============================================================================
# TODO 3: Auth - Reutilizar fluxo do Dia 2
# =============================================================================
# Copie do Dia 2 as funções verify_token/get_current_user ou importe se preferir.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def verify_token(token: str, expected_type: str = "access") -> dict:
    """
    Verifica e decodifica um token JWT.

    Args:
        token: Token JWT a verificar
        expected_type: Tipo esperado ("access" ou "refresh")

    Returns:
        dict: Payload do token

    Raises:
        HTTPException: Se token inválido ou expirado
    """

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
    return {
        "username": username,
        "payload": payload
    }


# =============================================================================
# TODO 4: Modelos Pydantic
# =============================================================================
class GenerateRequest(BaseModel):
    prompt: str = Field(..., description="Texto a ser enviado ao LLM")
    model: Optional[str] = Field(
        default=None,
        description="Modelo LLM (opcional)"
    )


class ChatRequest(BaseModel):
    message: str = Field(..., description="Mensagem do usuário")
    model: Optional[str] = Field(default=None, description="Modelo LLM")
    stream: bool = Field(
        default=True,
        description="Se true, responde via SSE"
    )


# =============================================================================
# TODO 5: Função de streaming do LLM
# =============================================================================
async def stream_llm(prompt: str, model: str) -> AsyncIterator[str]:
    """
    Gera tokens do LLM e envia em formato SSE.

    Formato SSE: yield f"data: {conteudo}\\n\\n"
    """
    # TODO: instanciar llm = ChatOpenAI(model=model, streaming=True)
    # TODO: iterar com async for chunk in llm.astream([HumanMessage(content=prompt)])
    # TODO: chunk.content pode vir vazio; pule tokens vazios
    # TODO: ao final, enviar "data: [DONE]\\n\\n"
    stream_llm = ChatOpenAI(
        model = model,
        temperature = 0.2,
        streaming = True,
    )

    human_message = HumanMessage(content = prompt)

    async for chunk in stream_llm.astream([human_message]):
        text = chunk.content
        if not text:
            continue
        yield f"data: {text}\n\n"
    
    yield "data: [DONE]\n\n"


FAKE_USER = {
    "username": "admin",
    "hashed_password": pwd_context.hash("admin123"),
}

# Funções auxiliares para hash e verificação
def hash_password(password: str) -> str:
    """Hash de senha usando bcrypt diretamente"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    """Verifica senha usando bcrypt diretamente"""
    try:
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
    except Exception:
        return False

# Modelo de Login
class LoginRequest(BaseModel):
    username: str = Field(description="Login de usuário")
    password: str = Field(description="Senha do usuário")

# Modelo de Refresh
class RefreshRequest(BaseModel):
    refresh_token: str = Field(description="Token de atualização")


# Gera Token de acesso
def create_access_token(data: dict, expires_delta=None) -> str:
    """
    Cria um access token JWT.

    Args:
        data: Dados a incluir no token (ex: {"sub": "username"})
        expires_delta: Tempo de expiração (opcional)

    Returns:
        str: Token JWT codificado
    """
    # TODO: Implementar
    # 1. to_encode = data.copy()
    # 2. Calcular expire (datetime.utcnow() + timedelta)
    # 3. to_encode.update({"exp": expire, "type": "access"})
    # 4. return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    to_encode = data.copy()
    time_utc = datetime.now(timezone.utc) 
    time_delta = timedelta(days = int(ACCESS_TOKEN_EXPIRE_MINUTES)) 
    expire = (time_utc + time_delta)
    to_encode.update({
        "exp": int(expire.timestamp()),
        "type": "access",
    })

    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm = JWT_ALGORITHM)


# Atualiza Token
def create_refresh_token(data: dict) -> str:
    """
    Cria um refresh token JWT.

    Args:
        data: Dados a incluir no token

    Returns:
        str: Token JWT codificado
    """
    
    to_encode = data.copy()
    time_utc = datetime.now(timezone.utc)
    time_delta = timedelta(days = int(REFRESH_TOKEN_EXPIRE_DAYS))
    expire = (time_utc + time_delta)
    to_encode.update({
        "exp": int(expire.timestamp()),
        "type": "refresh",
    })

    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm = JWT_ALGORITHM)


# Endpoint de Login
@app.post("/login", response_model=Token)
@limiter.limit("5/minute") # Máximo 5 tentativas por minuto
async def login(request: Request, login_data: LoginRequest):
    """
    Autentica usuário e retorna tokens JWT.

    Credenciais de teste:
    - username: admin
    - password: admin123
    """
    # TODO: Implementar
    # 1. Verificar se username existe
    # 2. Verificar senha com pwd_context.verify()
    # 3. Se inválido: raise HTTPException 401
    # 4. Criar tokens com create_access_token e create_refresh_token
    # 5. Retornar Token(access_token=..., refresh_token=...)

    if login_data.username != FAKE_USER["username"]:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Usuário inválido."
        )

    if not pwd_context.verify(login_data.password, FAKE_USER["hashed_password"]):
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            description = "Senha inválida."
        )

    access_token = create_access_token(data={"sub": login_data.username})
    refresh_token = create_refresh_token(data={"sub": login_data.username})

    return Token(
        access_token = access_token,
        refresh_token = refresh_token,
    )    


# Endpoint de Refres Token
@app.post("/refresh", response_model=Token)
async def refresh(request: RefreshRequest):
    """
    Renova tokens usando refresh token válido.
    """
    # TODO: Implementar
    # 1. payload = verify_token(request.refresh_token, expected_type="refresh")
    # 2. username = payload.get("sub")
    # 3. Criar novos tokens
    # 4. Retornar Token
    payload = verify_token(request.refresh_token, expected_type = "refresh")
    
    if not payload:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            description = "Não foi possível validar o token."
        )

    username = payload.get("sub")

    access_token = create_access_token(data = {"sub": username})
    refresh_token = create_refresh_token(data = {"sub": username})

    return Token(
        access_token = access_token,
        refresh_token = refresh_token,
    )


# Endpoint de Logout
@app.post("/logout")
async def logout(
    token: str = Depends(oauth2_scheme),
    current_user: dict = Depends(get_current_user)
):
    """
    Invalida o token atual (logout).
    """

    blacklist_token(token)
    return {"message": "Logout efetuado!"}

# Blacklist
token_blacklist: set = set()

def is_token_blacklisted(token: str) -> bool:
    """Verifica se token está na blacklist."""
    return token in token_blacklist

def blacklist_token(token: str) -> None:
    """Adiciona token à blacklist."""
    token_blacklist.add(token)

# =============================================================================
# TODO 6: Endpoint /api/generate (SSE)
# =============================================================================
@app.post("/api/generate")
async def generate(
    request: GenerateRequest,
    current_user: dict = Depends(get_current_user),
):
    """
    Endpoint principal de streaming (SSE).
    Retorna `text/event-stream` com tokens do LLM.
    """
    model = request.model or DEFAULT_MODEL
    generator = stream_llm(request.prompt, model=model)
    return StreamingResponse(generator, media_type="text/event-stream")


# =============================================================================
# TODO 7: Endpoint /chat (streaming opcional)
# =============================================================================
@app.post("/chat")
async def chat(
    request: ChatRequest,
    current_user: dict = Depends(get_current_user),
):
    """
    Se stream=True → retorna SSE.
    Se stream=False → retorna JSON com resposta completa.
    """
    model = request.model or DEFAULT_MODEL

    if request.stream:
        return StreamingResponse(
            stream_llm(request.message, model=model),
            media_type="text/event-stream",
        )

    # Modo não-stream: agrega os tokens
    llm = ChatOpenAI(model=model, streaming=True)
    ai_msg = await llm.ainvoke([HumanMessage(content=request.message)])
    return {
        "reply": ai_msg.content,
        "user": current_user["username"],
        "model": model,
    }


# =============================================================================
# Health check
# =============================================================================
@app.get("/health")
async def health():
    return {"status": "healthy", "feature": "streaming"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
