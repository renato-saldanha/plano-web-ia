# 📚 Guia de Aprendizado - Testes Automatizados com pytest

Este guia cobre os conceitos essenciais para implementar testes automatizados na API FastAPI usando pytest.

---

## 1. Introdução ao pytest

### O que é pytest?

**pytest** é um framework de testes para Python que facilita a escrita e execução de testes. É mais simples e poderoso que o módulo `unittest` padrão do Python.

### Por que usar pytest?

- **Sintaxe simples:** Testes são funções que começam com `test_`
- **Fixtures:** Sistema poderoso para setup e teardown
- **Assertions detalhadas:** Mostra diferenças quando testes falham
- **Plugins:** Extensível com plugins (cobertura, async, etc.)
- **Descoberta automática:** Encontra testes automaticamente

### Estrutura básica de um teste

```python
def test_exemplo():
    """Teste básico que verifica uma condição."""
    resultado = 2 + 2
    assert resultado == 4
```

### Executando testes

```bash
# Executar todos os testes
pytest

# Executar com mais detalhes
pytest -v

# Executar arquivo específico
pytest tests/test_auth.py

# Executar teste específico
pytest tests/test_auth.py::test_login_success
```

---

## 2. TestClient do FastAPI

### O que é TestClient?

**TestClient** é uma classe do FastAPI que permite testar sua aplicação sem precisar iniciar um servidor HTTP real. É baseado no `httpx` e simula requisições HTTP.

### Como usar TestClient

```python
from fastapi.testclient import TestClient
from template import app

# Criar cliente de teste
client = TestClient(app)

# Fazer requisição GET
response = client.get("/health")
assert response.status_code == 200
assert response.json() == {"status": "healthy"}

# Fazer requisição POST
response = client.post(
    "/login",
    json={"username": "admin", "password": "admin123"}
)
assert response.status_code == 200
data = response.json()
assert "access_token" in data
```

### Métodos do TestClient

- `client.get(url, **kwargs)` - Requisição GET
- `client.post(url, **kwargs)` - Requisição POST
- `client.put(url, **kwargs)` - Requisição PUT
- `client.delete(url, **kwargs)` - Requisição DELETE
- `client.patch(url, **kwargs)` - Requisição PATCH

### Parâmetros comuns

- `json={}` - Enviar JSON no body
- `headers={}` - Adicionar headers customizados
- `params={}` - Query parameters
- `files={}` - Upload de arquivos

### Exemplo completo

```python
def test_login_success(client: TestClient):
    """Testa login com credenciais válidas."""
    response = client.post(
        "/login",
        json={"username": "admin", "password": "admin123"}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert data["token_type"] == "bearer"
```

---

## 3. Fixtures do pytest

### O que são Fixtures?

**Fixtures** são funções que fornecem dados ou configurações para testes. Elas são executadas antes dos testes e podem ser reutilizadas.

### Criando uma fixture

```python
import pytest
from fastapi.testclient import TestClient
from template import app

@pytest.fixture
def client():
    """Fixture que retorna TestClient."""
    return TestClient(app)
```

### Usando fixtures em testes

```python
def test_health(client: TestClient):
    """Testa endpoint de health usando fixture."""
    response = client.get("/health")
    assert response.status_code == 200
```

### Fixtures com setup e teardown

```python
@pytest.fixture
def auth_headers(client: TestClient):
    """Fixture que faz login e retorna headers de autenticação."""
    # Setup: fazer login
    response = client.post(
        "/login",
        json={"username": "admin", "password": "admin123"}
    )
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    yield headers  # Retorna headers
    
    # Teardown: limpar (se necessário)
    # Neste caso, não há nada para limpar
```

### Fixtures compartilhadas (conftest.py)

Arquivo `tests/conftest.py` é carregado automaticamente pelo pytest e suas fixtures ficam disponíveis para todos os testes.

```python
# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from template import app

@pytest.fixture
def client():
    """Cliente de teste para a aplicação."""
    return TestClient(app)

@pytest.fixture
def auth_headers(client: TestClient):
    """Headers de autenticação para testes."""
    response = client.post(
        "/login",
        json={"username": "admin", "password": "admin123"}
    )
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}
```

### Escopo de fixtures

- `function` (padrão) - Executada uma vez por teste
- `class` - Executada uma vez por classe de testes
- `module` - Executada uma vez por módulo
- `session` - Executada uma vez por sessão de testes

```python
@pytest.fixture(scope="module")
def expensive_setup():
    """Setup caro executado uma vez por módulo."""
    # Código de setup
    yield resultado
    # Código de teardown
```

---

## 4. Testes de Autenticação

### Testando login

```python
def test_login_success(client: TestClient):
    """Testa login com credenciais válidas."""
    response = client.post(
        "/login",
        json={"username": "admin", "password": "admin123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data

def test_login_invalid_username(client: TestClient):
    """Testa login com usuário inválido."""
    response = client.post(
        "/login",
        json={"username": "invalid", "password": "admin123"}
    )
    assert response.status_code == 401
    assert "Usuário inválido" in response.json()["message"]

def test_login_invalid_password(client: TestClient):
    """Testa login com senha inválida."""
    response = client.post(
        "/login",
        json={"username": "admin", "password": "wrong"}
    )
    assert response.status_code == 401
    assert "Senha inválida" in response.json()["message"]
```

### Testando refresh token

```python
def test_refresh_token_success(client: TestClient, auth_headers: dict):
    """Testa refresh de token válido."""
    # Primeiro, obter refresh token
    login_response = client.post(
        "/login",
        json={"username": "admin", "password": "admin123"}
    )
    refresh_token = login_response.json()["refresh_token"]
    
    # Fazer refresh
    response = client.post(
        "/refresh",
        json={"refresh_token": refresh_token}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data

def test_refresh_token_invalid(client: TestClient):
    """Testa refresh com token inválido."""
    response = client.post(
        "/refresh",
        json={"refresh_token": "invalid_token"}
    )
    assert response.status_code == 401
```

### Testando proteção de rotas

```python
def test_protected_route_without_token(client: TestClient):
    """Testa acesso a rota protegida sem token."""
    response = client.get("/conversations")
    assert response.status_code == 401

def test_protected_route_with_invalid_token(client: TestClient):
    """Testa acesso a rota protegida com token inválido."""
    headers = {"Authorization": "Bearer invalid_token"}
    response = client.get("/conversations", headers=headers)
    assert response.status_code == 401

def test_protected_route_with_valid_token(client: TestClient, auth_headers: dict):
    """Testa acesso a rota protegida com token válido."""
    response = client.get("/conversations", headers=auth_headers)
    assert response.status_code == 200
```

---

## 5. Testes de Endpoints

### Testando criação de conversa

```python
def test_create_conversation(client: TestClient, auth_headers: dict):
    """Testa criação de nova conversa via "chat"."""
    response = client.post(
        "/chat",
        headers=auth_headers,
        json={
            "message": "Olá!",
            "stream": False
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "conversation_id" in data
    assert "reply" in data
```

### Testando envio de mensagem

```python
def test_send_message(client: TestClient, auth_headers: dict):
    """Testa envio de mensagem em conversa existente."""
    # Criar conversa
    response1 = client.post(
        "/chat",
        headers=auth_headers,
        json={"message": "Primeira mensagem", "stream": False}
    )
    conversation_id = response1.json()["conversation_id"]
    
    # Enviar segunda mensagem
    response2 = client.post(
        "/chat",
        headers=auth_headers,
        json={
            "message": "Segunda mensagem",
            "conversation_id": conversation_id,
            "stream": False
        }
    )
    assert response2.status_code == 200
    assert response2.json()["conversation_id"] == conversation_id
```

### Testando listagem de conversas

```python
def test_list_conversations(client: TestClient, auth_headers: dict):
    """Testa listagem de conversas do usuário."""
    # Criar algumas conversas
    for i in range(3):
        client.post(
            "/chat",
            headers=auth_headers,
            json={"message": f"Mensagem {i}", "stream": False}
        )
    
    # Listar conversas
    response = client.get("/conversations", headers=auth_headers)
    assert response.status_code == 200
    conversations = response.json()
    assert len(conversations) == 3
    assert all("id" in conv for conv in conversations)
    assert all("message_count" in conv for conv in conversations)
```

### Testando obtenção de mensagens

```python
def test_get_conversation_messages(client: TestClient, auth_headers: dict):
    """Testa obtenção de mensagens de uma conversa."""
    # Criar conversa com mensagens
    response1 = client.post(
        "/chat",
        headers=auth_headers,
        json={"message": "Mensagem 1", "stream": False}
    )
    conversation_id = response1.json()["conversation_id"]
    
    client.post(
        "/chat",
        headers=auth_headers,
        json={
            "message": "Mensagem 2",
            "conversation_id": conversation_id,
            "stream": False
        }
    )
    
    # Obter mensagens
    response = client.get(
        f"/conversations/{conversation_id}/messages",
        headers=auth_headers
    )
    assert response.status_code == 200
    messages = response.json()
    assert len(messages) == 4  # 2 user + 2 assistant
    assert messages[0]["role"] == "user"
    assert messages[1]["role"] == "assistant"
```

---

## 6. Testes de Rate Limiting

### Testando rate limit de login

```python
import time

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
    assert response.status_code == 429  # Too Many Requests
```

### Testando rate limit de chat

```python
def test_chat_rate_limit(client: TestClient, auth_headers: dict):
    """Testa rate limit de chat (30/min)."""
    # Fazer 30 requisições (limite)
    for i in range(30):
        response = client.post(
            "/chat",
            headers=auth_headers,
            json={"message": f"Test {i}", "stream": False}
        )
        assert response.status_code == 200
    
    # 31ª requisição deve ser bloqueada
    response = client.post(
        "/chat",
        headers=auth_headers,
        json={"message": "Should be blocked", "stream": False}
    )
    assert response.status_code == 429
```

### Testando rate limit por usuário

```python
def test_rate_limit_per_user(client: TestClient):
    """Testa que rate limit é por usuário, não global."""
    # Usuário 1 faz 30 requisições
    headers1 = client.post(
        "/login",
        json={"username": "admin", "password": "admin123"}
    ).json()
    auth_headers1 = {"Authorization": f"Bearer {headers1['access_token']}"}
    
    for i in range(30):
        response = client.post(
            "/chat",
            headers=auth_headers1,
            json={"message": f"User1 {i}", "stream": False}
        )
        assert response.status_code == 200
    
    # Usuário 2 ainda pode fazer requisições
    # (Nota: neste exemplo, temos apenas um usuário fake, então este teste
    # precisaria de múltiplos usuários para funcionar completamente)
```

---

## 7. Testes de Exception Handlers

### Testando HTTPException

```python
def test_http_exception_handler(client: TestClient):
    """Testa que HTTPException retorna JSON padronizado."""
    # Tentar acessar conversa inexistente
    auth_headers = client.post(
        "/login",
        json={"username": "admin", "password": "admin123"}
    ).json()
    headers = {"Authorization": f"Bearer {auth_headers['access_token']}"}
    
    response = client.get(
        "/conversations/invalid_id/messages",
        headers=headers
    )
    assert response.status_code == 404
    data = response.json()
    assert data["error"] == True
    assert "message" in data
    assert data["status_code"] == 404
    assert "path" in data
```

### Testando ValidationError

```python
def test_validation_error_handler(client: TestClient):
    """Testa que ValidationError retorna JSON com detalhes."""
    # Enviar requisição com dados inválidos
    response = client.post(
        "/login",
        json={"username": "admin"}  # Falta password
    )
    assert response.status_code == 422
    data = response.json()
    assert data["error"] == True
    assert "errors" in data
    assert len(data["errors"]) > 0
    assert "field" in data["errors"][0]
    assert "message" in data["errors"][0]
```

### Testando Exception genérica

```python
# Nota: Testar exception genérica requer simular um erro interno
# Isso pode ser feito mockando uma função para lançar exceção
# ou testando um endpoint que propositalmente falha

def test_generic_exception_handler(client: TestClient):
    """Testa que Exception genérica retorna mensagem genérica."""
    # Este teste requer simular um erro interno
    # Por exemplo, mockando uma dependência para falhar
    # Por enquanto, apenas verificamos que o handler existe
    pass
```

---

## 8. Cálculo de Cobertura

### Instalando pytest-cov

```bash
pip install pytest-cov
```

### Executando testes com cobertura

```bash
# Cobertura básica
pytest --cov=template

# Cobertura com relatório detalhado
pytest --cov=template --cov-report=term-missing

# Cobertura com relatório HTML
pytest --cov=template --cov-report=html

# Cobertura com limite mínimo
pytest --cov=template --cov-report=term-missing --cov-fail-under=60
```

### Interpretando relatório de cobertura

```
Name                    Stmts   Miss  Cover   Missing
-----------------------------------------------------
template.py               200     50    75%   45-50, 100-120
-----------------------------------------------------
TOTAL                     200     50    75%
```

- **Stmts:** Número de statements (linhas de código)
- **Miss:** Número de statements não executados
- **Cover:** Porcentagem de cobertura
- **Missing:** Linhas não cobertas

### Meta de cobertura

Para este projeto, a meta é **60% de cobertura**, focando em:
- Funcionalidades críticas (auth, chat, rate limiting)
- Exception handlers
- Endpoints principais

Não é necessário testar:
- Código de configuração
- Funções auxiliares simples
- Código de logging (se não for crítico)

---

## 9. Boas Práticas

### Organização de testes

- Um arquivo de teste por módulo/funcionalidade
- Nomes descritivos: `test_login_success`, `test_login_invalid_password`
- Agrupar testes relacionados em classes (opcional)

### Fixtures reutilizáveis

- Colocar fixtures comuns em `conftest.py`
- Usar escopo apropriado (function, module, session)
- Evitar fixtures muito complexas

### Assertions claras

```python
# Bom: Assertion clara
assert response.status_code == 200
assert "access_token" in response.json()

# Evitar: Assertions genéricas
assert response  # Muito vago
```

### Testes independentes

- Cada teste deve ser independente
- Não depender da ordem de execução
- Limpar estado entre testes (se necessário)

### Testes rápidos

- Evitar operações lentas (chamadas de API reais, I/O pesado)
- Usar mocks quando necessário
- Agrupar testes lentos separadamente

---

## 10. Recursos Adicionais

### Documentação oficial

- Pytest: https://docs.pytest.org/
- FastAPI Testing: https://fastapi.tiangolo.com/tutorial/testing/
- Pytest-cov: https://pytest-cov.readthedocs.io/
- Pytest-asyncio: https://pytest-asyncio.readthedocs.io/

### Comandos úteis

```bash
# Executar apenas testes que falharam na última execução
pytest --lf

# Executar testes em paralelo (requer pytest-xdist)
pytest -n auto

# Executar com output mais detalhado
pytest -vv

# Executar e parar no primeiro erro
pytest -x
```

---

**Última atualização:** 14 Dez 2025
