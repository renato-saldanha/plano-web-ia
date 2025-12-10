#!/usr/bin/env python3
"""
API FastAPI com Autenticação JWT - Exemplo de Referência Completo

Este arquivo contém a implementação completa para consulta.
Use como referência se travar em algum TODO do template.py.

⚠️ IMPORTANTE: Tente resolver os TODOs primeiro!
   Consulte este arquivo apenas se precisar de ajuda.

Uso:
    uvicorn exemplo_referencia:app --reload --port 8000

Teste:
    # Login
    curl -X POST http://localhost:8000/login \
        -H "Content-Type: application/json" \
        -d '{"username": "admin", "password": "admin123"}'
    
    # Chat protegido (com token)
    curl http://localhost:8000/chat \
        -H "Authorization: Bearer SEU_TOKEN_AQUI"
"""

# ============================================================================
# IMPORTS
# ============================================================================
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from passlib.context import CryptContext
from dotenv import load_dotenv
import os
import logging

# ============================================================================
# CONFIGURAÇÃO
# ============================================================================

# Carregar variáveis de ambiente
load_dotenv()

# Configurações JWT
SECRET_KEY = os.getenv("JWT_SECRET", "super_secret_key_change_in_production_123!")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "7"))

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configurar password hashing com bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Configurar OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# ============================================================================
# MODELOS PYDANTIC
# ============================================================================

class Token(BaseModel):
    """Modelo de resposta com tokens JWT."""
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class LoginRequest(BaseModel):
    """Modelo de requisição de login."""
    username: str
    password: str


class RefreshRequest(BaseModel):
    """Modelo de requisição de refresh token."""
    refresh_token: str


class ChatRequest(BaseModel):
    """Modelo de requisição de chat (opcional)."""
    message: str
    model: Optional[str] = "gpt-3.5-turbo"


class ChatResponse(BaseModel):
    """Modelo de resposta de chat."""
    response: str
    user: str
    model: str


# ============================================================================
# CONFIGURAÇÃO FASTAPI
# ============================================================================

app = FastAPI(
    title="API com JWT Auth",
    description="API FastAPI com autenticação JWT completa",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique origens permitidas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================================
# USUÁRIO FAKE (em produção, use banco de dados)
# ============================================================================

# Hash da senha "admin123"
FAKE_USER = {
    "username": "admin",
    "hashed_password": pwd_context.hash("admin123"),
    "email": "admin@example.com",
    "role": "admin"
}

# ============================================================================
# FUNÇÕES DE TOKEN
# ============================================================================

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Cria um access token JWT.
    
    Args:
        data: Dados a incluir no payload do token
        expires_delta: Tempo personalizado de expiração (opcional)
    
    Returns:
        str: Token JWT codificado
    
    Example:
        >>> token = create_access_token({"sub": "admin"})
        >>> print(token)  # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
    """
    to_encode = data.copy()
    
    # Definir tempo de expiração
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # Adicionar claims ao payload
    to_encode.update({
        "exp": expire,
        "iat": datetime.utcnow(),  # Issued at
        "type": "access"
    })
    
    # Codificar token
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    logger.info(f"Access token criado para: {data.get('sub')}")
    return encoded_jwt


def create_refresh_token(data: dict) -> str:
    """
    Cria um refresh token JWT com expiração mais longa.
    
    Args:
        data: Dados a incluir no payload do token
    
    Returns:
        str: Token JWT codificado
    """
    to_encode = data.copy()
    
    # Refresh token tem expiração mais longa
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    
    to_encode.update({
        "exp": expire,
        "iat": datetime.utcnow(),
        "type": "refresh"
    })
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    logger.info(f"Refresh token criado para: {data.get('sub')}")
    return encoded_jwt


def verify_token(token: str, expected_type: str = "access") -> dict:
    """
    Verifica e decodifica um token JWT.
    
    Args:
        token: Token JWT a verificar
        expected_type: Tipo esperado do token ("access" ou "refresh")
    
    Returns:
        dict: Payload decodificado do token
    
    Raises:
        HTTPException: Se token inválido, expirado ou tipo incorreto
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    
    try:
        # Decodificar token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        # Verificar tipo do token
        token_type = payload.get("type")
        if token_type != expected_type:
            logger.warning(f"Token type mismatch: expected {expected_type}, got {token_type}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Invalid token type. Expected {expected_type}."
            )
        
        # Verificar se tem subject
        username: str = payload.get("sub")
        if username is None:
            logger.warning("Token sem subject (sub)")
            raise credentials_exception
        
        logger.info(f"Token válido para: {username}")
        return payload
        
    except JWTError as e:
        logger.error(f"Erro ao verificar token: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"}
        )


# ============================================================================
# DEPENDENCY DE AUTENTICAÇÃO
# ============================================================================

async def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    """
    Dependency que extrai e valida o usuário atual do token.
    
    Esta função é usada com Depends() em rotas protegidas.
    Automaticamente extrai o token do header Authorization: Bearer <token>
    
    Args:
        token: Token JWT extraído automaticamente pelo oauth2_scheme
    
    Returns:
        dict: Informações do usuário autenticado
    
    Raises:
        HTTPException: Se token inválido ou usuário não encontrado
    
    Example:
        @app.get("/protected")
        async def protected_route(user: dict = Depends(get_current_user)):
            return {"message": f"Olá, {user['username']}!"}
    """
    # Verificar token
    payload = verify_token(token, expected_type="access")
    
    # Extrair username
    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload: missing subject"
        )
    
    # Em produção: buscar usuário no banco de dados
    # user = await db.get_user(username)
    # if user is None:
    #     raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "username": username,
        "payload": payload
    }


# ============================================================================
# ENDPOINTS
# ============================================================================

@app.get("/health")
async def health():
    """
    Health check - não requer autenticação.
    
    Útil para verificar se a API está rodando.
    """
    return {
        "status": "healthy",
        "auth": "jwt",
        "version": "1.0.0"
    }


@app.post("/login", response_model=Token)
async def login(request: LoginRequest):
    """
    Autentica usuário e retorna tokens JWT.
    
    Credenciais de teste:
    - username: admin
    - password: admin123
    
    Returns:
        Token: access_token, refresh_token, token_type
    
    Raises:
        HTTPException 401: Se credenciais inválidas
    """
    logger.info(f"Tentativa de login: {request.username}")
    
    # Verificar se usuário existe (em produção: consultar banco)
    if request.username != FAKE_USER["username"]:
        logger.warning(f"Usuário não encontrado: {request.username}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    # Verificar senha com bcrypt
    if not pwd_context.verify(request.password, FAKE_USER["hashed_password"]):
        logger.warning(f"Senha incorreta para: {request.username}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    # Gerar tokens
    access_token = create_access_token(data={"sub": request.username})
    refresh_token = create_refresh_token(data={"sub": request.username})
    
    logger.info(f"Login bem-sucedido: {request.username}")
    
    return Token(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="bearer"
    )


@app.post("/refresh", response_model=Token)
async def refresh(request: RefreshRequest):
    """
    Renova tokens usando um refresh token válido.
    
    Use este endpoint quando o access token expirar.
    O refresh token também é renovado para manter a sessão ativa.
    
    Returns:
        Token: Novos access_token e refresh_token
    
    Raises:
        HTTPException 401: Se refresh token inválido ou expirado
    """
    logger.info("Tentativa de refresh token")
    
    # Verificar refresh token
    payload = verify_token(request.refresh_token, expected_type="refresh")
    
    # Extrair username
    username = payload.get("sub")
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token: missing subject"
        )
    
    # Em produção: verificar se usuário ainda existe e está ativo
    # user = await db.get_user(username)
    # if user is None or not user.is_active:
    #     raise HTTPException(status_code=401, detail="User not found or inactive")
    
    # Gerar novos tokens
    access_token = create_access_token(data={"sub": username})
    refresh_token = create_refresh_token(data={"sub": username})
    
    logger.info(f"Tokens renovados para: {username}")
    
    return Token(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="bearer"
    )


@app.get("/chat")
async def chat(current_user: dict = Depends(get_current_user)):
    """
    Endpoint de chat protegido por autenticação JWT.
    
    Requer header: Authorization: Bearer <access_token>
    
    Este é um placeholder - em produção, integraria com LLM.
    
    Returns:
        dict: Mensagem de eco com informações do usuário
    """
    username = current_user["username"]
    
    logger.info(f"Chat acessado por: {username}")
    
    return {
        "message": f"Olá, {username}! Esta rota está protegida por JWT.",
        "user": username,
        "authenticated": True,
        "token_info": {
            "type": current_user["payload"].get("type"),
            "issued_at": current_user["payload"].get("iat"),
            "expires_at": current_user["payload"].get("exp")
        }
    }


@app.post("/chat", response_model=ChatResponse)
async def chat_post(
    request: ChatRequest,
    current_user: dict = Depends(get_current_user)
):
    """
    Endpoint de chat com POST - envia mensagem (placeholder).
    
    Em produção, integraria com LLM (OpenAI, Claude, etc.)
    
    Requer header: Authorization: Bearer <access_token>
    """
    username = current_user["username"]
    
    logger.info(f"Chat POST de {username}: {request.message[:50]}...")
    
    # Placeholder - em produção, chamaria LLM
    response_text = f"Echo: {request.message}"
    
    return ChatResponse(
        response=response_text,
        user=username,
        model=request.model
    )


# ============================================================================
# ENDPOINT DE DEBUG (remover em produção)
# ============================================================================

@app.get("/debug/token-info")
async def debug_token_info(current_user: dict = Depends(get_current_user)):
    """
    Debug endpoint - mostra informações do token atual.
    
    ⚠️ REMOVER EM PRODUÇÃO!
    """
    return {
        "user": current_user["username"],
        "payload": current_user["payload"],
        "config": {
            "algorithm": ALGORITHM,
            "access_expire_minutes": ACCESS_TOKEN_EXPIRE_MINUTES,
            "refresh_expire_days": REFRESH_TOKEN_EXPIRE_DAYS
        }
    }


# ============================================================================
# EXECUÇÃO
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    
    print("=" * 60)
    print("API com JWT Auth - Exemplo de Referência")
    print("=" * 60)
    print(f"Docs: http://localhost:8000/docs")
    print(f"Credenciais teste: admin / admin123")
    print("=" * 60)
    
    uvicorn.run(app, host="0.0.0.0", port=8000)


