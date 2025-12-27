# 🧭 GUIA_PASSO_A_PASSO - Rate Limiting e Logging (Nível 1)

**Objetivo:** Implementar rate limiting por usuário e logging estruturado na API FastAPI.

---

## 📚 Conceitos que você vai aprender

### 1. Rate Limiting por Usuário
- **O que é:** Limitar número de requisições por usuário autenticado (não por IP)
- **Por que:** Mais seguro que rate limiting por IP, previne abuso mesmo com IP compartilhado
- **Como:** Usar `slowapi` com função customizada que extrai `user_id` do token JWT

### 2. Logging Estruturado
- **O que é:** Logs em formato JSON, fácil de processar e analisar
- **Por que:** Facilita monitoramento, debugging e análise de logs em produção
- **Como:** Usar `JSONFormatter` customizado e função helper `log_structured()`

### 3. Middleware de Request Logging
- **O que é:** Middleware que loga automaticamente todas as requisições
- **Por que:** Rastreabilidade completa: método, path, status, tempo de resposta
- **Como:** Criar middleware customizado que captura informações da requisição

---

## 🚀 Passo 1: Preparar Ambiente (10min)

### 1.1 Ativar ambiente virtual
```powershell
# PowerShell
./venv/Scripts/Activate.ps1

# Bash
source venv/bin/activate
```

### 1.2 Instalar dependências
```bash
pip install -r requirements.txt
```

**Dependências necessárias:**
- `slowapi` - Rate limiting
- `fastapi` - Framework web
- `python-jose` - JWT tokens
- `passlib` - Password hashing
- `langchain-openai` - Integração com LLM

### 1.3 Verificar variáveis de ambiente
Crie ou verifique `.env` na raiz do projeto:
```env
JWT_SECRET_KEY=sua_chave_secreta_aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
OPENAI_API_KEY=sua_chave_openai
```

---

## 🚀 Passo 2: Entender Rate Limiting por Usuário (15min)

### 2.1 O que é Rate Limiting?
Rate limiting limita o número de requisições que um cliente pode fazer em um período de tempo.

**Exemplo:**
- Sem rate limiting: Usuário pode fazer 1000 requisições/segundo
- Com rate limiting (30/min): Usuário pode fazer no máximo 30 requisições por minuto

### 2.2 Rate Limiting por IP vs por Usuário

**Por IP (padrão):**
```python
limiter = Limiter(key_func=get_remote_address)  # Usa IP do cliente
```
- ❌ Problema: Múltiplos usuários no mesmo IP compartilham limite
- ❌ Problema: Usuário pode mudar IP para burlar limite

**Por Usuário (melhor):**
```python
def get_user_id_for_rate_limit(request: Request) -> str:
    # Extrai user_id do token JWT
    # Se não houver token, usa IP como fallback
    return user_id

limiter = Limiter(key_func=get_user_id_for_rate_limit)
```
- ✅ Cada usuário tem seu próprio limite
- ✅ Mais seguro e justo

### 2.3 Como funciona `get_user_id_for_rate_limit()`

```python
def get_user_id_for_rate_limit(request: Request) -> str:
    # 1. Tentar extrair token do header Authorization
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        # Se não houver token, usar IP como fallback
        return get_remote_address(request)
    
    # 2. Extrair token do header
    token = auth_header.split(" ")[1]
    
    # 3. Decodificar token JWT
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        user_id = payload.get("sub")  # "sub" contém o username
        return user_id or get_remote_address(request)
    except Exception:
        # Se houver erro, usar IP como fallback
        return get_remote_address(request)
```

**Fluxo:**
1. Função é chamada pelo `slowapi` para cada requisição
2. Tenta extrair `user_id` do token JWT
3. Se não conseguir, usa IP como fallback
4. `slowapi` usa o retorno como chave para rastrear rate limits

---

## 🚀 Passo 3: Entender Logging Estruturado (15min)

### 3.1 O que é Logging Estruturado?

**Logging tradicional:**
```
2025-12-13 10:30:45 INFO Usuário admin fez login
```
- ❌ Difícil de processar programaticamente
- ❌ Difícil de filtrar e analisar

**Logging estruturado (JSON):**
```json
{"timestamp":"2025-12-13T10:30:45Z","level":"INFO","message":"Login bem-sucedido","user_id":"admin"}
```
- ✅ Fácil de processar (é JSON!)
- ✅ Fácil de filtrar por campos
- ✅ Fácil de enviar para sistemas de monitoramento

### 3.2 JSONFormatter

O `JSONFormatter` converte logs do Python em JSON:

```python
class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_data = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }
        
        # Adicionar campos extras se existirem
        if hasattr(record, "user_id"):
            log_data["user_id"] = record.user_id
        
        return json.dumps(log_data)
```

### 3.3 Função `log_structured()`

Helper para facilitar logging estruturado:

```python
log_structured("INFO", "Login bem-sucedido", user_id="admin")
# Output: {"timestamp":"...","level":"INFO","message":"Login bem-sucedido","user_id":"admin"}
```

**Vantagens:**
- Sempre inclui timestamp
- Sempre em formato JSON
- Fácil de adicionar campos extras

---

## 🚀 Passo 4: Implementar Rate Limiting (30min)

### 4.1 Importar dependências

```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from jose import jwt
```

### 4.2 Criar função `get_user_id_for_rate_limit()`

```python
def get_user_id_for_rate_limit(request: Request) -> str:
    """
    Extrai user_id do token JWT para usar como chave de rate limiting.
    Se não houver token, usa IP como fallback.
    """
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return get_remote_address(request)
    
    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        user_id = payload.get("sub")
        return user_id or get_remote_address(request)
    except Exception:
        return get_remote_address(request)
```

### 4.3 Configurar Limiter

```python
limiter = Limiter(key_func=get_user_id_for_rate_limit)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
```

### 4.4 Aplicar Rate Limit aos Endpoints

```python
@app.post("/login")
@limiter.limit("5/minute")  # 5 tentativas de login por minuto
async def login(request: Request, login_data: LoginRequest):
    # ...

@app.post("/chat")
@limiter.limit("30/minute")  # 30 requisições de chat por minuto por usuário
async def chat(request: Request, chat_request: ChatRequest, ...):
    # ...
```

**Importante:** O decorator `@limiter.limit()` deve vir ANTES do decorator `@app.post()`.

---

## 🚀 Passo 5: Implementar Logging Estruturado (25min)

### 5.1 Usar módulo compartilhado

```python
# Importar do módulo compartilhado
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from common.logging import JSONFormatter, log_structured, setup_logger

# Configurar logger
logger = setup_logger(__name__)
```

### 5.2 Usar `log_structured()` nos endpoints

```python
@app.post("/login")
async def login(request: Request, login_data: LoginRequest):
    # ... lógica de login ...
    
    # Logar login bem-sucedido
    log_structured("INFO", "Login bem-sucedido", user_id=login_data.username)
    
    return Token(...)

@app.post("/chat")
async def chat(request: Request, chat_request: ChatRequest, ...):
    # Logar início de chat
    log_structured(
        "INFO",
        "Início de chat",
        user_id=user_id,
        conversation_id=conversation_id,
        model=model
    )
    
    try:
        # ... lógica do chat ...
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
```

---

## 🚀 Passo 6: Criar Middleware de Request Logging (20min)

### 6.1 Criar classe do Middleware

```python
import time
from starlette.middleware.base import BaseHTTPMiddleware

class RequestLoggingMiddleware(BaseHTTPMiddleware):
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
```

### 6.2 Registrar Middleware

```python
app.add_middleware(RequestLoggingMiddleware)
```

**Importante:** Middlewares são executados na ordem inversa de registro. Se você registrar `RequestLoggingMiddleware` depois de outros middlewares, ele será executado primeiro.

---

## 🚀 Passo 7: Testar Implementação (15min)

### 7.1 Iniciar servidor

```bash
uvicorn exemplo_completo:app --reload --port 8000
```

### 7.2 Testar Rate Limiting

**Teste 1: Login com rate limit**
```bash
# Fazer 6 requisições de login rapidamente
for i in {1..6}; do
  curl -X POST http://localhost:8000/login \
    -H "Content-Type: application/json" \
    -d '{"username":"admin","password":"admin123"}'
done
```

**Esperado:**
- Primeiras 5 requisições: Status 200 (sucesso)
- 6ª requisição: Status 429 (Too Many Requests)

**Teste 2: Chat com rate limit por usuário**
```bash
# 1. Fazer login e obter token
TOKEN=$(curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}' | jq -r '.access_token')

# 2. Fazer 31 requisições de chat rapidamente
for i in {1..31}; do
  curl -X POST http://localhost:8000/chat \
    -H "Authorization: Bearer $TOKEN" \
    -H "Content-Type: application/json" \
    -d '{"message":"teste"}'
done
```

**Esperado:**
- Primeiras 30 requisições: Status 200 (sucesso)
- 31ª requisição: Status 429 (Too Many Requests)

### 7.3 Verificar Logs Estruturados

Os logs devem aparecer no console em formato JSON:

```json
{"timestamp":"2025-12-13T10:30:45Z","level":"INFO","message":"Request processada","method":"POST","path":"/chat","status_code":200,"duration_ms":1234.56}
{"timestamp":"2025-12-13T10:30:46Z","level":"INFO","message":"Início de chat","user_id":"admin","conversation_id":"abc-123","model":"gpt-4o-mini"}
```

---

## ✅ Checklist de Verificação

- [ X] Função `get_user_id_for_rate_limit()` criada e funcionando
- [ X] Limiter configurado com função customizada
- [ X] Rate limit aplicado ao endpoint `/login` (5/min)
- [ X] Rate limit aplicado ao endpoint `/chat` (30/min)
- [ X] Logger configurado com `JSONFormatter`
- [ X] Função `log_structured()` sendo usada nos endpoints
- [ X] Middleware `RequestLoggingMiddleware` criado e registrado
- [ X] Testes de rate limiting passando
- [ X] Logs aparecendo em formato JSON

---

## 🎯 Próximos Passos

No **Dia 6**, você vai aprender:
- Testes automatizados com pytest
- Exception handlers globais (tratamento de erros)

---

## 📚 Referências

- SlowAPI: https://slowapi.readthedocs.io/
- Python Logging: https://docs.python.org/3/library/logging.html
- FastAPI Middleware: https://fastapi.tiangolo.com/advanced/middleware/
- Módulos compartilhados: `../common/README.md`

