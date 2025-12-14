# 📚 Guia de Aprendizado - Dia 5

## Rate Limiting, Exception Handling e Logging Estruturado

Este guia explica os conceitos necessários para implementar rate limiting por usuário, tratamento robusto de erros e logging estruturado na API FastAPI.

---

## 1. Rate Limiting por Usuário

### 1.1 Conceito

Rate limiting é uma técnica que limita o número de requisições que um cliente pode fazer em um período de tempo. No Dia 2, implementamos rate limiting por IP usando `slowapi`. Hoje, vamos implementar rate limiting **por usuário**, que é mais seguro e preciso.

**Por que rate limiting por usuário?**
- Previne abuso mesmo quando múltiplos usuários compartilham o mesmo IP
- Permite limites diferentes por tipo de usuário (ex: premium vs free)
- Mais preciso para APIs que exigem autenticação

### 1.2 Implementação com SlowAPI

SlowAPI permite usar uma função customizada para determinar a chave de rate limiting. Em vez de usar o IP do cliente, podemos usar o `user_id` extraído do token JWT.

**Passo 1: Criar função para extrair user_id**

```python
from fastapi import Request, Depends
from slowapi.util import get_remote_address

def get_user_id_for_rate_limit(request: Request) -> str:
    """
    Extrai user_id do token JWT para usar como chave de rate limiting.
    Se não houver token, usa IP como fallback.
    """
    # Tentar extrair token do header Authorization
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        # Fallback para IP se não houver token
        return get_remote_address(request)
    
    token = auth_header.split(" ")[1]
    try:
        # Decodificar JWT (sem verificar assinatura completa, apenas para extrair user_id)
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        user_id = payload.get("sub")  # username do usuário
        return user_id or get_remote_address(request)
    except Exception:
        # Se falhar, usar IP como fallback
        return get_remote_address(request)
```

**Passo 2: Configurar Limiter com função customizada**

```python
from slowapi import Limiter

limiter = Limiter(key_func=get_user_id_for_rate_limit)
app.state.limiter = limiter
```

**Passo 3: Aplicar rate limit aos endpoints**

```python
@app.post("/chat")
@limiter.limit("30/minute")  # 30 requisições por minuto por usuário
async def chat(
    request: Request,  # Request deve ser primeiro parâmetro para slowapi
    chat_request: ChatRequest,
    current_user: dict = Depends(get_current_user),
):
    # ... código do endpoint
```

**⚠️ Importante:**
- O parâmetro `Request` deve ser o primeiro parâmetro do endpoint quando usar `@limiter.limit()`
- A função `get_user_id_for_rate_limit()` deve retornar uma string única por usuário

### 1.3 Testando Rate Limiting

Para testar, faça múltiplas requisições rápidas:

```bash
# Fazer 31 requisições rápidas
for i in {1..31}; do
  curl -X POST http://localhost:8000/chat \
    -H "Authorization: Bearer $TOKEN" \
    -H "Content-Type: application/json" \
    -d '{"message": "test"}'
done
```



A 31ª requisição deve retornar status 429 (Too Many Requests).

---

## 2. Exception Handlers Globais

### 2.1 Conceito

Exception handlers globais permitem tratar todos os erros de forma consistente, retornando respostas JSON padronizadas. Isso melhora a experiência do cliente e facilita o debug.

**Tipos de erros comuns:**
- `HTTPException`: Erros HTTP explícitos (404, 401, etc.)
- `ValidationError`: Erros de validação do Pydantic
- `Exception`: Erros inesperados (500)

### 2.2 Implementação

**Handler para HTTPException:**

```python
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """
    Trata HTTPException retornando JSON padronizado.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": True,
            "message": exc.detail,
            "status_code": exc.status_code,
            "path": str(request.url.path),
        }
    )
```

**Handler para ValidationError (Pydantic):**

```python
from pydantic import ValidationError
from fastapi.exceptions import RequestValidationError

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Trata erros de validação do Pydantic.
    """
    errors = []
    for error in exc.errors():
        errors.append({
            "field": ".".join(str(loc) for loc in error["loc"]),
            "message": error["msg"],
            "type": error["type"],
        })
    
    return JSONResponse(
        status_code=422,
        content={
            "error": True,
            "message": "Erro de validação",
            "errors": errors,
            "status_code": 422,
            "path": str(request.url.path),
        }
    )
```

**Handler para Exception genérica (catch-all):**

```python
import logging

logger = logging.getLogger(__name__)

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """
    Trata erros inesperados (catch-all).
    IMPORTANTE: Logar erro completo, mas retornar mensagem genérica ao cliente.
    """
    # Logar erro completo (com stack trace) para debug
    logger.error(
        f"Erro inesperado: {exc}",
        exc_info=True,  # Inclui stack trace
        extra={
            "path": str(request.url.path),
            "method": request.method,
        }
    )
    
    # Retornar mensagem genérica ao cliente (não expor detalhes internos)
    return JSONResponse(
        status_code=500,
        content={
            "error": True,
            "message": "Erro interno do servidor",
            "status_code": 500,
            "path": str(request.url.path),
        }
    )
```

**⚠️ Importante:**
- Sempre logar erros completos no servidor
- Nunca expor detalhes internos (stack traces, paths de arquivos) ao cliente
- Retornar mensagens genéricas mas úteis

---

## 3. Logging Estruturado

### 3.1 Conceito

Logging estruturado usa formato JSON em vez de texto livre, facilitando análise e monitoramento. Cada log é um objeto JSON com campos padronizados.

**Vantagens:**
- Fácil parsing e busca
- Permite filtrar por campos específicos
- Compatível com ferramentas de monitoramento (ELK, Datadog, etc.)

### 3.2 Configuração Básica

```python
import logging
import json
from datetime import datetime

# Configurar formato JSON
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
        if hasattr(record, "conversation_id"):
            log_data["conversation_id"] = record.conversation_id
        
        return json.dumps(log_data)

# Configurar logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)
```

### 3.3 Função Helper para Logging Estruturado

```python
def log_structured(level: str, message: str, **kwargs):
    """
    Função helper para logging estruturado.
    
    Args:
        level: Nível do log (INFO, WARNING, ERROR, etc.)
        message: Mensagem do log
        **kwargs: Campos extras para incluir no log
    """
    log_data = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "level": level,
        "message": message,
        **kwargs
    }
    
    log_json = json.dumps(log_data)
    
    if level == "ERROR":
        logger.error(log_json)
    elif level == "WARNING":
        logger.warning(log_json)
    else:
        logger.info(log_json)
```

### 3.4 Uso Prático

```python
# Log de login bem-sucedido
log_structured("INFO", "Login bem-sucedido", user_id=username)

# Log de início de chat
log_structured(
    "INFO",
    "Início de chat",
    user_id=user_id,
    conversation_id=conversation_id,
    model=model_name
)

# Log de erro
log_structured(
    "ERROR",
    "Erro ao processar chat",
    user_id=user_id,
    error=str(exc),
    conversation_id=conversation_id
)
```

---

## 4. Middleware de Request Logging

### 4.1 Conceito

Middleware de request logging registra todas as requisições HTTP, incluindo método, path, status code e tempo de resposta. Isso fornece visibilidade completa do tráfego da API.

### 4.2 Implementação

```python
from starlette.middleware.base import BaseHTTPMiddleware
import time

class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Capturar tempo inicial
        start_time = time.time()
        
        # Processar requisição
        response = await call_next(request)
        
        # Calcular duração
        duration = time.time() - start_time
        
        # Logar requisição
        log_structured(
            "INFO",
            "Request processada",
            method=request.method,
            path=str(request.url.path),
            status_code=response.status_code,
            duration_ms=round(duration * 1000, 2),  # Converter para milissegundos
            client_ip=request.client.host if request.client else None,
        )
        
        return response

# Registrar middleware
app.add_middleware(RequestLoggingMiddleware)
```

**⚠️ Importante:**
- Registrar middleware **depois** de outros middlewares (CORS, etc.)
- Não logar dados sensíveis (senhas, tokens completos)
- Converter duração para milissegundos para facilitar leitura

---

## 5. Boas Práticas

### 5.1 Rate Limiting
- Use limites razoáveis (ex: 30/minuto para chat, 5/minuto para login)
- Implemente fallback para IP quando não houver autenticação
- Documente limites na documentação da API

### 5.2 Exception Handling
- Sempre logar erros completos no servidor
- Nunca expor detalhes internos ao cliente
- Retornar mensagens úteis mas genéricas
- Usar status codes HTTP apropriados

### 5.3 Logging
- Use níveis apropriados (INFO, WARNING, ERROR)
- Inclua contexto relevante (user_id, conversation_id, etc.)
- Não logue dados sensíveis
- Use formato JSON para facilitar parsing

### 5.4 Middleware
- Registre middleware na ordem correta
- Não bloqueie requisições no middleware (use async/await)
- Logue apenas informações necessárias

---

## 6. Referências

- SlowAPI Documentation: https://slowapi.readthedocs.io/
- FastAPI Exception Handling: https://fastapi.tiangolo.com/tutorial/handling-errors/
- Python Logging: https://docs.python.org/3/library/logging.html
- FastAPI Middleware: https://fastapi.tiangolo.com/advanced/middleware/

---

**Próximo passo:** Implementar essas funcionalidades no `template.py` seguindo os TODOs.
