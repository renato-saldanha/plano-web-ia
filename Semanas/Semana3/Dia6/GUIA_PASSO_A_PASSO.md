# 🧭 GUIA_PASSO_A_PASSO - Testes com pytest e Exception Handling (Nível 1)

**Objetivo:** Implementar testes automatizados com pytest e exception handlers básicos na API FastAPI.

---

## 📚 Conceitos que você vai aprender

### 1. pytest (Conceito Novo)
- **O que é:** Framework de testes para Python
- **Por que:** Garante que código funciona corretamente e previne regressões
- **Como:** Escrever funções de teste que verificam comportamento esperado

### 2. TestClient (FastAPI)
- **O que é:** Cliente de teste que simula requisições HTTP
- **Por que:** Testa endpoints sem precisar rodar servidor
- **Como:** Criar instância de TestClient e fazer requisições

### 3. Fixtures (pytest)
- **O que é:** Funções que preparam dados para testes
- **Por que:** Evita duplicação e garante setup consistente
- **Como:** Criar funções com decorator `@pytest.fixture`

### 4. Exception Handlers Básicos
- **O que é:** Tratamento global de erros HTTP
- **Por que:** Respostas consistentes e melhor UX
- **Como:** Usar `@app.exception_handler()` para registrar handlers

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
- `pytest` - Framework de testes
- `pytest-cov` - Cobertura de código
- `httpx` - Cliente HTTP (já incluído no FastAPI)
- `fastapi` - Framework web
- Outras dependências do Dia 5

### 1.3 Verificar estrutura de testes
Certifique-se de que existe a pasta `tests/` com:
- `__init__.py` (pode estar vazio)
- `conftest.py` (fixtures compartilhadas)
- Arquivos de teste (`test_*.py`)

---

## 🚀 Passo 2: Entender pytest (20min)

### 2.1 O que é pytest?

**pytest** é um framework de testes para Python que facilita escrever e executar testes.

**Estrutura básica de um teste:**
```python
def test_nome_do_teste():
    # Arrange: Preparar dados
    valor = 2 + 2
    
    # Act: Executar ação
    resultado = valor
    
    # Assert: Verificar resultado
    assert resultado == 4
```

**Regras:**
- Funções de teste devem começar com `test_`
- Usar `assert` para verificar condições
- Se `assert` falhar, o teste falha

### 2.2 Executar testes

```bash
# Executar todos os testes
pytest

# Executar testes em arquivo específico
pytest tests/test_auth.py

# Executar teste específico
pytest tests/test_auth.py::test_login

# Executar com output detalhado
pytest -v

# Executar com cobertura
pytest --cov=. --cov-report=term-missing
```

### 2.3 Estrutura de um teste completo

```python
def test_login_success(client: TestClient):
    """
    Testa login bem-sucedido.
    
    Arrange: Preparar dados de login
    Act: Fazer requisição POST /login
    Assert: Verificar status 200 e presença de tokens
    """
    # Arrange
    login_data = {"username": "admin", "password": "admin123"}
    
    # Act
    response = client.post("/login", json=login_data)
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data
```

---

## 🚀 Passo 3: Entender TestClient (15min)

### 3.1 O que é TestClient?

**TestClient** é uma classe do FastAPI que simula requisições HTTP sem precisar rodar um servidor real.

**Vantagens:**
- Testes rápidos (sem overhead de servidor)
- Fácil de usar (mesma API de cliente HTTP)
- Testa toda a stack FastAPI (middlewares, dependencies, etc.)

### 3.2 Criar TestClient

```python
from fastapi.testclient import TestClient
from template import app  # ou exemplo_completo

# Criar cliente de teste
client = TestClient(app)
```

### 3.3 Fazer requisições

```python
# GET request
response = client.get("/health")
assert response.status_code == 200

# POST request
response = client.post(
    "/login",
    json={"username": "admin", "password": "admin123"}
)
assert response.status_code == 200

# POST com headers
response = client.post(
    "/chat",
    headers={"Authorization": f"Bearer {token}"},
    json={"message": "Hello"}
)
```

### 3.4 Verificar resposta

```python
# Status code
assert response.status_code == 200

# JSON response
data = response.json()
assert data["status"] == "healthy"

# Headers
assert "Content-Type" in response.headers
```

---

## 🚀 Passo 4: Entender Fixtures (15min)

### 4.1 O que são Fixtures?

**Fixtures** são funções que preparam dados ou recursos para testes. Elas evitam duplicação e garantem setup consistente.

### 4.2 Criar Fixtures

**Arquivo `tests/conftest.py`:**
```python
import pytest
from fastapi.testclient import TestClient
from template import app

@pytest.fixture
def client():
    """Fixture que cria um TestClient."""
    return TestClient(app)

@pytest.fixture
def auth_headers(client: TestClient):
    """Fixture que retorna headers de autenticação."""
    # Fazer login
    response = client.post(
        "/login",
        json={"username": "admin", "password": "admin123"}
    )
    token = response.json()["access_token"]
    
    # Retornar headers
    return {"Authorization": f"Bearer {token}"}
```

### 4.3 Usar Fixtures

```python
def test_chat(client: TestClient, auth_headers: dict):
    """Teste que usa fixtures."""
    response = client.post(
        "/chat",
        headers=auth_headers,
        json={"message": "Hello"}
    )
    assert response.status_code == 200
```

**Como funciona:**
1. pytest encontra função `test_chat`
2. Verifica parâmetros: `client` e `auth_headers`
3. Procura fixtures com esses nomes
4. Executa fixtures antes do teste
5. Passa resultados como parâmetros

---

## 🚀 Passo 5: Implementar Exception Handlers Básicos (20min)

### 5.1 O que são Exception Handlers?

**Exception Handlers** são funções que tratam erros globalmente, retornando respostas JSON consistentes.

### 5.2 Handler para HTTPException

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

**Quando é chamado:**
- Quando você faz `raise HTTPException(status_code=404, detail="Not found")`
- Handler captura e retorna JSON formatado

### 5.3 Handler para RequestValidationError

```python
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

**Quando é chamado:**
- Quando dados da requisição não passam na validação do Pydantic
- Handler formata erros de validação de forma clara

---

## 🚀 Passo 6: Escrever Testes Básicos (70min)

### 6.1 Testes de Autenticação (20min)

**Arquivo `tests/test_auth.py`:**
```python
def test_login_success(client: TestClient):
    """Testa login bem-sucedido."""
    response = client.post(
        "/login",
        json={"username": "admin", "password": "admin123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data

def test_login_invalid_username(client: TestClient):
    """Testa login com username inválido."""
    response = client.post(
        "/login",
        json={"username": "invalid", "password": "admin123"}
    )
    assert response.status_code == 401
    data = response.json()
    assert data["error"] == True
    assert "Usuário inválido" in data["message"]

def test_login_invalid_password(client: TestClient):
    """Testa login com senha inválida."""
    response = client.post(
        "/login",
        json={"username": "admin", "password": "wrong"}
    )
    assert response.status_code == 401
```

### 6.2 Testes de Chat Básico (25min)

**Arquivo `tests/test_chat.py`:**
```python
def test_chat_success(client: TestClient, auth_headers: dict):
    """Testa chat bem-sucedido."""
    response = client.post(
        "/chat",
        headers=auth_headers,
        json={"message": "Hello", "stream": False}
    )
    assert response.status_code == 200
    data = response.json()
    assert "reply" in data
    assert "conversation_id" in data

def test_chat_unauthorized(client: TestClient):
    """Testa chat sem autenticação."""
    response = client.post(
        "/chat",
        json={"message": "Hello"}
    )
    assert response.status_code == 401
```

### 6.3 Testes de Rate Limiting Básico (15min)

**Arquivo `tests/test_rate_limiting.py`:**
```python
def test_login_rate_limit(client: TestClient):
    """Testa rate limit de login (5/min)."""
    # Fazer 5 requisições (limite)
    for i in range(5):
        response = client.post(
            "/login",
            json={"username": "admin", "password": "admin123"}
        )
        assert response.status_code == 200
    
    # 6ª requisição deve ser bloqueada
    response = client.post(
        "/login",
        json={"username": "admin", "password": "admin123"}
    )
    assert response.status_code == 429
```

### 6.4 Testes de Exception Handlers (10min)

**Arquivo `tests/test_exceptions.py`:**
```python
def test_http_exception_handler(client: TestClient):
    """Testa handler de HTTPException."""
    # Endpoint que não existe retorna 404
    response = client.get("/endpoint_inexistente")
    assert response.status_code == 404
    data = response.json()
    assert data["error"] == True
    assert "status_code" in data

def test_validation_error_handler(client: TestClient):
    """Testa handler de ValidationError."""
    # Dados inválidos (faltando campo obrigatório)
    response = client.post(
        "/login",
        json={"username": "admin"}  # Falta "password"
    )
    assert response.status_code == 422
    data = response.json()
    assert data["error"] == True
    assert "errors" in data
```

---

## 🚀 Passo 7: Executar Testes e Verificar Cobertura (15min)

### 7.1 Executar todos os testes

```bash
pytest
```

**Saída esperada:**
```
tests/test_auth.py::test_login_success PASSED
tests/test_chat.py::test_chat_success PASSED
...
```

### 7.2 Verificar cobertura

```bash
pytest --cov=. --cov-report=term-missing
```

**Saída esperada:**
```
Name                    Stmts   Miss  Cover   Missing
-----------------------------------------------------
template.py               200     50    75%   45-60, 120-130
-----------------------------------------------------
TOTAL                     200     50    75%
```

**Meta:** Alcançar pelo menos 60% de cobertura focando em funcionalidades críticas.

### 7.3 Corrigir testes que falharam

Se algum teste falhar:
1. Leia a mensagem de erro
2. Verifique o que o teste esperava vs. o que recebeu
3. Corrija o código ou o teste
4. Execute novamente

---

## ✅ Checklist de Verificação

- [ x] pytest instalado e funcionando
- [ x] Estrutura `tests/` criada
- [ x] `conftest.py` com fixtures básicas
- [ ] Testes de autenticação criados e passando
- [ ] Testes de chat básico criados e passando
- [ ] Testes de rate limiting básico criados e passando
- [ ] Exception handlers básicos implementados
- [ ] Testes de exception handlers criados e passando
- [ ] Cobertura mínima de 60% alcançada
- [ ] Todos os testes passando

---

## 🎯 Próximos Passos

No **Dia 7**, você vai aprender:
- Configurar Swagger/OpenAPI
- Deploy em produção (Railway)

---

## 📚 Referências

- Pytest Documentation: https://docs.pytest.org/
- FastAPI Testing: https://fastapi.tiangolo.com/tutorial/testing/
- Pytest Fixtures: https://docs.pytest.org/en/stable/fixture.html
- Pytest-cov: https://pytest-cov.readthedocs.io/
- FastAPI Exception Handling: https://fastapi.tiangolo.com/tutorial/handling-errors/

