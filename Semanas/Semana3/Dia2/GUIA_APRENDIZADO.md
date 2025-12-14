# 📚 Guia de Aprendizado - Autenticação JWT com FastAPI

Este guia explica os conceitos de JWT e como implementá-los no FastAPI. 
**Leia as seções 1-3 ANTES de começar a implementar.**

---

## 📖 PARTE 1: TEORIA (Leia primeiro!)

> ⚠️ **Esta parte é para LEITURA. Não escreva código ainda.**

---

### Seção 1: O que é JWT (5 min de leitura)

#### 1.1 Definição
JWT (JSON Web Token) é um padrão aberto (RFC 7519) para transmitir informações de forma segura entre partes como um objeto JSON. O token é assinado digitalmente, garantindo sua integridade.

#### 1.2 Estrutura do JWT
Um JWT tem 3 partes separadas por pontos:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

| Parte | Conteúdo | Exemplo Decodificado |
|-------|----------|---------------------|
| **Header** | Algoritmo e tipo | `{"alg": "HS256", "typ": "JWT"}` |
| **Payload** | Dados (claims) | `{"sub": "user123", "exp": 1234567890}` |
| **Signature** | Assinatura | `HMACSHA256(header + payload, secret)` |

#### 1.3 Access Token vs Refresh Token

| Tipo | Duração | Uso | Armazenamento |
|------|---------|-----|---------------|
| **Access Token** | Curta (15-60 min) | Autorizar requisições | Header Authorization |
| **Refresh Token** | Longa (7-30 dias) | Obter novo access token | Cookie HttpOnly ou storage seguro |

**Por que dois tokens?**
- Access token curto = se vazado, janela de ataque é pequena
- Refresh token longo = usuário não precisa fazer login toda hora
- Refresh token é usado APENAS para renovar, nunca para acessar recursos

#### 1.4 Claims Importantes

```json
{
  "sub": "user123",      // Subject - identificador do usuário
  "exp": 1702234567,     // Expiration - quando expira (Unix timestamp)
  "iat": 1702230967,     // Issued At - quando foi criado
  "type": "access"       // Tipo do token (custom claim)
}
```

---

### Seção 2: JWT no FastAPI (5 min de leitura)

#### 2.1 OAuth2PasswordBearer
FastAPI tem um helper para extrair tokens do header `Authorization: Bearer <token>`:

```python
from fastapi.security import OAuth2PasswordBearer

# tokenUrl é o endpoint de login (para documentação OpenAPI)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
```

Quando usado como dependency, ele:
1. Procura o header `Authorization: Bearer <token>`
2. Extrai o token
3. Retorna o token como string
4. Se não encontrar, retorna 401 automaticamente

#### 2.2 Depends() para Proteção
O `Depends()` do FastAPI permite criar "guards" para rotas:

```python
from fastapi import Depends

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # Esta função recebe o token automaticamente
    # Aqui você valida o token e retorna o usuário
    user = verify_token(token)
    return user

@app.get("/protected")
async def protected_route(user: dict = Depends(get_current_user)):
    # Esta rota só é acessível com token válido
    # O usuário já vem validado
    return {"message": f"Olá, {user['sub']}!"}
```

#### 2.3 Fluxo de Autenticação

```
┌─────────────┐     POST /login      ┌─────────────┐
│   Cliente   │ ─────────────────────▶│   Servidor  │
│  (Frontend) │   {user, password}   │  (FastAPI)  │
└─────────────┘                       └─────────────┘
                                            │
                                            ▼
                                      Valida credenciais
                                      Gera access + refresh
                                            │
┌─────────────┐   {access, refresh}   ┌─────────────┐
│   Cliente   │ ◀─────────────────────│   Servidor  │
└─────────────┘                       └─────────────┘
       │
       │ GET /chat
       │ Authorization: Bearer <access_token>
       ▼
┌─────────────┐                       ┌─────────────┐
│   Cliente   │ ─────────────────────▶│   Servidor  │
└─────────────┘                       └─────────────┘
                                            │
                                            ▼
                                      Valida access_token
                                      Processa requisição
                                            │
┌─────────────┐       Resposta        ┌─────────────┐
│   Cliente   │ ◀─────────────────────│   Servidor  │
└─────────────┘                       └─────────────┘
```

---

### Seção 3: Password Hashing (5 min de leitura)

#### 3.1 Por que não guardar senhas em texto?
Se o banco de dados for comprometido:
- **Texto puro:** Atacante tem todas as senhas
- **Hash simples (MD5/SHA):** Atacante usa rainbow tables
- **Hash com salt (bcrypt):** Cada senha tem salt único, muito mais seguro

#### 3.2 bcrypt
bcrypt é um algoritmo de hashing projetado para senhas:
- Inclui salt automaticamente
- É intencionalmente lento (dificulta força bruta)
- Configurável (work factor)

```python
from passlib.context import CryptContext

# Configurar contexto de hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Criar hash de senha (ao cadastrar usuário)
hashed = pwd_context.hash("senha123")
# Resultado: "$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/X4.OAG.V7Y7xX.V6u"

# Verificar senha (ao fazer login)
is_valid = pwd_context.verify("senha123", hashed)  # True
is_valid = pwd_context.verify("outra_senha", hashed)  # False
```

#### 3.3 Fluxo de Cadastro e Login

**Cadastro:**
```
senha_texto → bcrypt.hash() → hash_armazenado_no_banco
```

**Login:**
```
senha_digitada + hash_do_banco → bcrypt.verify() → True/False
```

---

## 🔧 PARTE 2: PRÁTICA (Agora sim, implemente!)

> ✅ **Agora você pode abrir o `template.py` e começar a implementar.**

---

### Seção 4: Implementando Passo a Passo

#### 4.1 Imports Necessários

```python
# FastAPI
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware

# Pydantic para validação
from pydantic import BaseModel

# JWT
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional

# Password hashing
from passlib.context import CryptContext

# Variáveis de ambiente
from dotenv import load_dotenv
import os
```

#### 4.2 Configuração do Ambiente

Crie um arquivo `.env` na raiz:
```env
JWT_SECRET=sua_chave_secreta_muito_longa_e_aleatoria_aqui
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
```

No código:
```python
load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET", "fallback_secret_key")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "7"))
```

#### 4.3 Modelos Pydantic

```python
class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class LoginRequest(BaseModel):
    username: str
    password: str

class RefreshRequest(BaseModel):
    refresh_token: str
```

#### 4.4 Criando Tokens

```python
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({
        "exp": expire,
        "type": "access"
    })
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def create_refresh_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    
    to_encode.update({
        "exp": expire,
        "type": "refresh"
    })
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
```

#### 4.5 Verificando Tokens

```python
def verify_token(token: str, expected_type: str = "access") -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        # Verificar tipo do token
        token_type = payload.get("type")
        if token_type != expected_type:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Token type invalid. Expected {expected_type}, got {token_type}"
            )
        
        return payload
        
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Could not validate token: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"}
        )
```

#### 4.6 Dependency de Autenticação

```python
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    payload = verify_token(token, expected_type="access")
    
    username = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload"
        )
    
    return {"username": username, "payload": payload}
```

#### 4.7 Endpoints

```python
# Usuário fake para testes (em produção, consulte banco de dados)
FAKE_USER = {
    "username": "admin",
    "hashed_password": pwd_context.hash("admin123")
}

@app.post("/login", response_model=Token)
async def login(request: LoginRequest):
    # Verifica usuário (em produção: consultar banco)
    if request.username != FAKE_USER["username"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    
    # Verifica senha
    if not pwd_context.verify(request.password, FAKE_USER["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    
    # Gera tokens
    access_token = create_access_token(data={"sub": request.username})
    refresh_token = create_refresh_token(data={"sub": request.username})
    
    return Token(
        access_token=access_token,
        refresh_token=refresh_token
    )

@app.post("/refresh", response_model=Token)
async def refresh(request: RefreshRequest):
    # Verificar refresh token
    payload = verify_token(request.refresh_token, expected_type="refresh")
    
    username = payload.get("sub")
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token"
        )
    
    # Gerar novos tokens
    access_token = create_access_token(data={"sub": username})
    refresh_token = create_refresh_token(data={"sub": username})
    
    return Token(
        access_token=access_token,
        refresh_token=refresh_token
    )

@app.get("/chat")
async def chat(current_user: dict = Depends(get_current_user)):
    return {
        "message": f"Olá, {current_user['username']}! Esta rota está protegida.",
        "user": current_user
    }
```

---

## 📚 Referências

- FastAPI Security: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
- python-jose: https://python-jose.readthedocs.io/
- passlib: https://passlib.readthedocs.io/
- JWT.io (debugger): https://jwt.io/
- RFC 7519 (JWT): https://datatracker.ietf.org/doc/html/rfc7519

---

**Última atualização:** 10 Dez 2025


