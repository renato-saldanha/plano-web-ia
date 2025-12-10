# 🏋️ Exercícios - Dia 2 (JWT Authentication)

Exercícios extras para praticar e aprofundar os conceitos de autenticação JWT.
**Complete apenas se sobrar tempo no buffer ou após o dia.**

---

## Exercício 1: Hardening de Segurança (Básico)

### Objetivo
Melhorar a segurança da implementação básica.

### Tarefas

1. **Configurar CORS estrito**
   - Substitua `allow_origins=["*"]` por origens específicas
   - Adicione validação de headers

```python
# De:
allow_origins=["*"]

# Para:
allow_origins=[
    "http://localhost:3000",  # Frontend dev
    "https://meusite.com"     # Produção
]
```

2. **Adicionar headers de segurança**
   - Crie um middleware que adiciona headers de segurança

```python
from starlette.middleware.base import BaseHTTPMiddleware

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        return response

app.add_middleware(SecurityHeadersMiddleware)
```

3. **Validar força da senha**
   - Crie uma função que valida requisitos mínimos de senha

```python
import re

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
```

### Teste
- Tente acessar de origem não permitida
- Verifique headers de resposta no navegador (F12 > Network)

---

## Exercício 2: Token Blacklist (Intermediário)

### Objetivo
Implementar invalidação de tokens (logout real).

### Contexto
JWT é stateless - uma vez emitido, é válido até expirar. Para implementar logout, precisamos de uma blacklist.

### Tarefas

1. **Criar estrutura de blacklist** (em memória para teste)

```python
# Em produção, use Redis ou banco de dados
token_blacklist: set = set()

def is_token_blacklisted(token: str) -> bool:
    """Verifica se token está na blacklist."""
    return token in token_blacklist

def blacklist_token(token: str) -> None:
    """Adiciona token à blacklist."""
    token_blacklist.add(token)
```

2. **Modificar verify_token para checar blacklist**

```python
def verify_token(token: str, expected_type: str = "access") -> dict:
    # Adicionar no início:
    if is_token_blacklisted(token):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has been revoked"
        )
    
    # ... resto da função
```

3. **Criar endpoint de logout**

```python
@app.post("/logout")
async def logout(
    token: str = Depends(oauth2_scheme),
    current_user: dict = Depends(get_current_user)
):
    """
    Invalida o token atual (logout).
    """
    blacklist_token(token)
    return {"message": "Successfully logged out"}
```

### Teste
```bash
# Login
TOKEN=$(curl -s -X POST http://localhost:8000/login \
    -H "Content-Type: application/json" \
    -d '{"username": "admin", "password": "admin123"}' | jq -r '.access_token')

# Verificar acesso
curl http://localhost:8000/chat -H "Authorization: Bearer $TOKEN"

# Logout
curl -X POST http://localhost:8000/logout -H "Authorization: Bearer $TOKEN"

# Tentar acessar novamente (deve falhar)
curl http://localhost:8000/chat -H "Authorization: Bearer $TOKEN"
```

---

## Exercício 3: Rate Limiting (Intermediário)

### Objetivo
Proteger endpoint de login contra ataques de força bruta.

### Tarefas

1. **Instalar slowapi**
```bash
pip install slowapi
```

2. **Implementar rate limiting**

```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.post("/login")
@limiter.limit("5/minute")  # Máximo 5 tentativas por minuto
async def login(request: Request, login_data: LoginRequest):
    # ... implementação
```

### Teste
```bash
# Fazer mais de 5 requisições em 1 minuto
for i in {1..10}; do
    curl -X POST http://localhost:8000/login \
        -H "Content-Type: application/json" \
        -d '{"username": "admin", "password": "wrong"}'
    echo ""
done
# Após a 5ª, deve retornar 429 Too Many Requests
```

---

## Exercício 4: Clock Skew Tolerance (Avançado)

### Objetivo
Lidar com diferenças de relógio entre cliente e servidor.

### Contexto
Se o relógio do servidor estiver alguns segundos diferente do cliente, tokens podem parecer inválidos. A solução é adicionar tolerância.

### Tarefas

1. **Adicionar leeway na verificação**

```python
def verify_token(token: str, expected_type: str = "access") -> dict:
    try:
        # Adicionar leeway de 30 segundos
        payload = jwt.decode(
            token, 
            SECRET_KEY, 
            algorithms=[ALGORITHM],
            options={
                "leeway": 30  # Tolerância de 30 segundos
            }
        )
        # ... resto
```

2. **Adicionar claim `nbf` (not before)**

```python
def create_access_token(data: dict, expires_delta=None) -> str:
    to_encode = data.copy()
    now = datetime.utcnow()
    
    to_encode.update({
        "exp": now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
        "iat": now,
        "nbf": now - timedelta(seconds=30),  # Válido desde 30s atrás
        "type": "access"
    })
    # ...
```

---

## Exercício 5: Refresh Token Rotation (Avançado)

### Objetivo
Implementar rotação de refresh tokens para maior segurança.

### Contexto
Cada vez que um refresh token é usado, ele é invalidado e um novo é gerado. Se alguém roubar um refresh token antigo, não conseguirá usar.

### Tarefas

1. **Armazenar família de tokens**

```python
# Em produção, use Redis ou banco
refresh_token_families: dict = {}  # {username: {current_token, used_tokens}}

def create_refresh_token_with_family(data: dict) -> str:
    """Cria refresh token e registra na família."""
    token = create_refresh_token(data)
    username = data.get("sub")
    
    if username not in refresh_token_families:
        refresh_token_families[username] = {"current": None, "used": set()}
    
    refresh_token_families[username]["current"] = token
    return token
```

2. **Verificar e rotacionar no refresh**

```python
@app.post("/refresh")
async def refresh(request: RefreshRequest):
    payload = verify_token(request.refresh_token, expected_type="refresh")
    username = payload.get("sub")
    
    family = refresh_token_families.get(username, {})
    
    # Se token já foi usado, invalidar toda a família (possível roubo)
    if request.refresh_token in family.get("used", set()):
        refresh_token_families[username] = {"current": None, "used": set()}
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token reuse detected. All tokens revoked."
        )
    
    # Marcar token atual como usado
    if request.refresh_token == family.get("current"):
        family["used"].add(request.refresh_token)
    
    # Gerar novos tokens
    access_token = create_access_token(data={"sub": username})
    new_refresh_token = create_refresh_token_with_family(data={"sub": username})
    
    return Token(access_token=access_token, refresh_token=new_refresh_token)
```

---

## 📊 Critérios de Avaliação

| Exercício | Dificuldade | Tempo Estimado | Pontos |
|-----------|-------------|----------------|--------|
| 1. Hardening | Básico | 20 min | 10 |
| 2. Blacklist | Intermediário | 30 min | 20 |
| 3. Rate Limiting | Intermediário | 25 min | 20 |
| 4. Clock Skew | Avançado | 15 min | 15 |
| 5. Token Rotation | Avançado | 40 min | 35 |

**Meta:** Complete pelo menos os exercícios 1 e 2 se tiver tempo extra.

---

## 📚 Referências

- OWASP JWT Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html
- FastAPI Security Best Practices: https://fastapi.tiangolo.com/tutorial/security/
- slowapi (rate limiting): https://github.com/laurents/slowapi

---

**Última atualização:** 10 Dez 2025


