#!/usr/bin/env python3
"""
API FastAPI com Autenticação JWT - Template

Este template contém TODOs para você completar.
Consulte GUIA_APRENDIZADO.md para entender os conceitos.
Consulte exemplo_referencia.py se precisar de ajuda.

Uso:
    uvicorn template:app --reload --port 8000
"""

# ============================================================================
# TODO 1: IMPORTS
# ============================================================================
# Importe as bibliotecas necessárias:
# - FastAPI, Depends, HTTPException, status (de fastapi)
# - OAuth2PasswordBearer (de fastapi.security)
# - CORSMiddleware (de fastapi.middleware.cors)
# - BaseModel (de pydantic)
# - JWTError, jwt (de jose)
# - datetime, timedelta (de datetime)
# - Optional (de typing)
# - CryptContext (de passlib.context)
# - load_dotenv (de dotenv)
# - os
#
# Dica: Consulte GUIA_APRENDIZADO.md seção 4.1

import os
import bcrypt
import re

from fastapi import FastAPI, Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from dotenv import load_dotenv
from starlette.status import HTTP_401_UNAUTHORIZED
from starlette.middleware.base import BaseHTTPMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded


# ============================================================================
# TODO 2: CARREGAR VARIÁVEIS DE AMBIENTE
# ============================================================================
# Use load_dotenv() e os.getenv() para carregar:
# - JWT_SECRET (chave secreta)
# - JWT_ALGORITHM (algoritmo, padrão HS256)
# - ACCESS_TOKEN_EXPIRE_MINUTES (expiração do access token)
# - REFRESH_TOKEN_EXPIRE_DAYS (expiração do refresh token)
#
# Dica: Consulte GUIA_APRENDIZADO.md seção 4.2

# TODO: Carregar variáveis de ambiente
# load_dotenv()

# Carrega o .env
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


# ============================================================================
# TODO 3: CONFIGURAR PASSWORD HASHING
# ============================================================================
# Configure o CryptContext com bcrypt
#
# Dica: pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# TODO: Configurar pwd_context

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

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)

# ============================================================================
# CONFIGURAÇÃO DO FASTAPI (já pronto)
# ============================================================================
app = FastAPI(
    title="API com JWT Auth",
    description="API FastAPI com autenticação JWT",
    version="1.0.0"
)


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


ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost"
]

# CORS (já configurado do Dia 1)
app.add_middleware(
    CORSMiddleware,    
    allow_origins=[ALLOWED_ORIGINS],  # Em produção, especifique origens
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(SecurityHeadersMiddleware)

# Configuração de Rate Limiter báscio, Max 5/Min
limiter = Limiter(key_func = get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# ============================================================================
# TODO 4: MODELOS PYDANTIC - Token
# ============================================================================
# Crie o modelo Token com:
# - access_token: str
# - refresh_token: str
# - token_type: str (padrão "bearer")
#
# Dica: Consulte GUIA_APRENDIZADO.md seção 4.3

class Token(BaseModel):
    access_token: str = Field(description="Token de acesso")
    refresh_token: str = Field(description="Token de atualização")
    token_type: str = Field(description="Tipo de token", default="bearer")


# ============================================================================
# TODO 5: MODELOS PYDANTIC - LoginRequest e RefreshRequest
# ============================================================================
# Crie o modelo LoginRequest com:
# - username: str
# - password: str
#
# Crie o modelo RefreshRequest com:
# - refresh_token: str

class LoginRequest(BaseModel):
    username: str = Field(description="Login de usuário")
    password: str = Field(description="Senha do usuário")


class RefreshRequest(BaseModel):
    refresh_token: str = Field(description="Token de atualização")


# ============================================================================
# TODO 6: FUNÇÃO create_access_token
# ============================================================================
# Crie uma função que:
# 1. Copia os dados recebidos
# 2. Adiciona "exp" (expiração) e "type": "access"
# 3. Codifica com jwt.encode()
# 4. Retorna o token
#
# Dica: Consulte GUIA_APRENDIZADO.md seção 4.4

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


# ============================================================================
# TODO 7: FUNÇÃO create_refresh_token
# ============================================================================
# Similar ao access token, mas:
# - Expiração mais longa (REFRESH_TOKEN_EXPIRE_DAYS)
# - "type": "refresh"
#
# Dica: Consulte GUIA_APRENDIZADO.md seção 4.4

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


# ============================================================================
# TODO 8: FUNÇÃO verify_token
# ============================================================================
# Crie uma função que:
# 1. Decodifica o token com jwt.decode()
# 2. Verifica se o tipo do token é o esperado
# 3. Retorna o payload se válido
# 4. Lança HTTPException 401 se inválido
#
# Dica: Consulte GUIA_APRENDIZADO.md seção 4.5

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
    # TODO: Implementar
    # Use try/except para capturar JWTError
    
    try:
        if is_token_blacklisted(token):
            raise HTTPException(
                status_code = HTTP_401_UNAUTHORIZED,
                description = "Token revogado."
            )

        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms = [JWT_ALGORITHM])

        token_type = payload.get("type")
        if token_type != expected_type:
            raise HTTPException(
                status_code = HTTP_401_UNAUTHORIZED,
                description = f"Tipo de token inválido. Esperado {expected_type}, temos {token_type}"
            )
        
        return payload
    except JWTError as j:
        raise HTTPException(
            status_code = HTTP_401_UNAUTHORIZED,
            description = f"Não foi possível validar o token: {str(j)}",
            headers = {"WWW-Authenticate": "Bearer"}
        )
    except Exception as e:
        raise Exception(f"Erro inesperado: {e}")



# ============================================================================
# TODO 9: CONFIGURAR OAuth2PasswordBearer
# ============================================================================
# Configure o scheme de autenticação
#
# Dica: oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# TODO: Configurar oauth2_scheme


oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "login")

# ============================================================================
# TODO 10: DEPENDENCY get_current_user
# ============================================================================
# Crie uma função que:
# 1. Recebe o token via Depends(oauth2_scheme)
# 2. Verifica o token com verify_token()
# 3. Extrai o username do payload
# 4. Retorna um dict com informações do usuário
#
# Dica: Consulte GUIA_APRENDIZADO.md seção 4.6

async def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:  
    """
    Dependency que extrai e valida o usuário atual do token.

    Args:
        token: Token JWT extraído do header Authorization

    Returns:
        dict: Informações do usuário autenticado
    """
    # TODO: Implementar
    # 1. payload = verify_token(token, expected_type="access")
    # 2. username = payload.get("sub")
    # 3. if not username: raise HTTPException 401
    # 4. return {"username": username, "payload": payload}
    
    payload = verify_token(token, expected_type = "access")
    username = payload.get("sub")
    if not username: 
        raise HTTPException(
                status_code = HTTP_401_UNAUTHORIZED,
                detail = "Usuário não autorizado."
            )
    
    return {
        "username": username,
        "payload": payload,
    }


# ============================================================================
# USUÁRIO FAKE PARA TESTES (já pronto)
# ============================================================================
# Em produção, consulte um banco de dados real
# O hash abaixo é para a senha "admin123"
FAKE_USER = {
    "username": "admin",
    # TODO: Descomente a linha abaixo após configurar pwd_context
    "hashed_password": pwd_context.hash("admin123"),
    # "hashed_password": "senha_hash_aqui"  # Temporário
}

def validate_password_strength(password: str) -> bool:
    """
    Valida se a senha atende aos requisitos:
    - Mínimo 8 caracteres
    - Pelo menos 1 letra maiúscula
    - Pelo menos 1 letra minúscula
    - Pelo menos 1 número
    """

    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    return True


# ============================================================================
# TODO 11: ENDPOINT POST /login
# ============================================================================
# Crie um endpoint que:
# 1. Recebe LoginRequest (username, password)
# 2. Verifica se usuário existe (use FAKE_USER por enquanto)
# 3. Verifica senha com pwd_context.verify()
# 4. Gera access e refresh tokens
# 5. Retorna modelo Token
#
# Dica: Consulte GUIA_APRENDIZADO.md seção 4.7


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


# ============================================================================
# TODO 12: ENDPOINT POST /refresh
# ============================================================================
# Crie um endpoint que:
# 1. Recebe RefreshRequest (refresh_token)
# 2. Verifica o refresh token
# 3. Extrai o username
# 4. Gera novos tokens
# 5. Retorna modelo Token
#
# Dica: Consulte GUIA_APRENDIZADO.md seção 4.7

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


# ============================================================================
# TODO 13: PROTEGER ENDPOINT /chat
# ============================================================================
# Modifique o endpoint /chat para:
# 1. Adicionar dependency: current_user: dict = Depends(get_current_user)
# 2. Usar current_user na resposta
#
# Dica: Apenas adicione o parâmetro com Depends

@app.get("/chat")
    # TODO: Adicionar current_user: dict = Depends(get_current_user)
async def chat(current_user: dict = Depends(get_current_user)):  
    """
    Endpoint de chat protegido por autenticação.

    Requer header: Authorization: Bearer <access_token>
    """
    # TODO: Modificar para usar current_user
    return {
        "message": "Esta rota deve estar protegida!",
        "user": current_user["username"]  # Descomente após implementar
    }


# ============================================================================
# ENDPOINT /health (já pronto - do Dia 1)
# ============================================================================
@app.get("/health")
async def health():
    """Health check - não requer autenticação."""
    return {"status": "healthy", "auth": "jwt"}


@app.post("/logout")
async def logout(
    token: str = Depends(oauth2_scheme),
    current_user: dict = Depends(get_current_user)
):
    """
    Invalida o token atual (logout).
    """

    blacklist_token(token)
    return {"message": "Logou efetuado!"}


# Blacklist
token_blacklist: set = set()

def is_token_blacklisted(token: str) -> bool:
    """Verifica se token está na blacklist."""
    return token in token_blacklist

def blacklist_token(token: str) -> None:
    """Adiciona token à blacklist."""
    token_blacklist.add(token)
    

# ============================================================================
# EXECUÇÃO
# ============================================================================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
