import uuid
import pytest
from fastapi.testclient import TestClient
from template import app, conversations

# Cache global para o token de autenticação
_auth_token_cache = None


@pytest.fixture(scope="function")
def client():
    """
    Client da aplicação com isolamento para cada teste.
    """

    client = TestClient(app)
    # gera id unico e curto
    test_id = str(uuid.uuid4())[:8]

    original_request = client.request

    def request_with_test_id(*args, **kwargs):
        if kwargs.get("headers") is None:
            kwargs["headers"] = {}
        if "headers" not in kwargs:
            kwargs["headers"] = {}
        # Adiciona o X-Test-ID 
        kwargs["headers"]["X-Test-ID"] = test_id
        return original_request(*args, **kwargs)

    client.request = request_with_test_id
    return client


@pytest.fixture(scope="session")
def test_user():
    """
    Retorna usuário válido para testes.
    """

    user_json = {"username": "admin", "password": "admin123"}
    return user_json


def _get_auth_token(client, test_user):
    """
    Função auxiliar para obter token de autenticação.
    Usa cache global para evitar múltiplas requisições.
    """

    response = client.post("/login", json=test_user)
    if response.status_code != 200:
        raise ValueError(
            f"Falha ao obter token de autenticação. "
            f"Status: {response.status_code}, Resposta: {response.text}"
        )
    data = response.json()
    _auth_token_cache = data["access_token"]

    return _auth_token_cache


@pytest.fixture(scope="function")
def auth_headers(client, test_user):
    """
    Retorna headers de autenticação para testes.
    Usa cache para garantir que o token seja obtido apenas uma vez.
    """
    response = client.post("/login", json=test_user)
    if response.status_code != 200:
        raise ValueError(
            f"Falha ao obter token de autenticação. "
            f"Status: {response.status_code}, Resposta: {response.text}"
        )
    data = response.json()
    token = data["access_token"]

    headers = {"Authorization": f"Bearer {token}"}

    # Adiciona X-Test-ID para manter isolamento
    test_id = client.request.__self__.headers.get("X-Test-ID") if hasattr(client.request, '__self__') else None
    if test_id:
        headers["X-Test-ID"] = test_id

    return headers


@pytest.fixture(autouse=True)
def clear_conversations():
    """
    Limpa as conversas antes de cada teste.
    """

    conversations.clear()
    yield
    conversations.clear()


@pytest.fixture
def test_user_invalid_username():
    """
    Retorna usuário com username inválido para testes.
    """

    user_json = {"username": "wrong", "password": "admin123"}
    return user_json


@pytest.fixture
def test_user_invalid_password():
    """
    Retorna usuário com senha inválida para testes.
    """

    user_json = {"username": "admin", "password": "wrong"}
    return user_json
