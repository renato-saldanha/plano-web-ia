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

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
# TODO: Adicione os imports que faltam aqui



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

SECRET_KEY = "chave_temporaria_mude_isso"  # TODO: Use os.getenv()
ALGORITHM = "HS256"  # TODO: Use os.getenv()
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # TODO: Use os.getenv()
REFRESH_TOKEN_EXPIRE_DAYS = 7  # TODO: Use os.getenv()


# ============================================================================
# TODO 3: CONFIGURAR PASSWORD HASHING
# ============================================================================
# Configure o CryptContext com bcrypt
#
# Dica: pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# TODO: Configurar pwd_context


# ============================================================================
# CONFIGURAÇÃO DO FASTAPI (já pronto)
# ============================================================================
app = FastAPI(
    title="API com JWT Auth",
    description="API FastAPI com autenticação JWT",
    version="1.0.0"
)

# CORS (já configurado do Dia 1)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique origens
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    # TODO: Adicione os campos aqui
    pass


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
    # TODO: Adicione os campos aqui
    pass


class RefreshRequest(BaseModel):
    # TODO: Adicione o campo aqui
    pass


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
    pass


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
    # TODO: Implementar
    pass


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
    pass


# ============================================================================
# TODO 9: CONFIGURAR OAuth2PasswordBearer
# ============================================================================
# Configure o scheme de autenticação
#
# Dica: oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# TODO: Configurar oauth2_scheme


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

async def get_current_user(token: str = None) -> dict:  # TODO: Adicionar Depends
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
    pass


# ============================================================================
# USUÁRIO FAKE PARA TESTES (já pronto)
# ============================================================================
# Em produção, consulte um banco de dados real
# O hash abaixo é para a senha "admin123"
FAKE_USER = {
    "username": "admin",
    # TODO: Descomente a linha abaixo após configurar pwd_context
    # "hashed_password": pwd_context.hash("admin123")
    "hashed_password": "senha_hash_aqui"  # Temporário
}


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
async def login(request: LoginRequest):
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
    pass


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
    pass


# ============================================================================
# TODO 13: PROTEGER ENDPOINT /chat
# ============================================================================
# Modifique o endpoint /chat para:
# 1. Adicionar dependency: current_user: dict = Depends(get_current_user)
# 2. Usar current_user na resposta
#
# Dica: Apenas adicione o parâmetro com Depends

@app.get("/chat")
async def chat():  # TODO: Adicionar current_user: dict = Depends(get_current_user)
    """
    Endpoint de chat protegido por autenticação.
    
    Requer header: Authorization: Bearer <access_token>
    """
    # TODO: Modificar para usar current_user
    return {
        "message": "Esta rota deve estar protegida!",
        # "user": current_user["username"]  # Descomente após implementar
    }


# ============================================================================
# ENDPOINT /health (já pronto - do Dia 1)
# ============================================================================
@app.get("/health")
async def health():
    """Health check - não requer autenticação."""
    return {"status": "healthy", "auth": "jwt"}


# ============================================================================
# EXECUÇÃO
# ============================================================================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


