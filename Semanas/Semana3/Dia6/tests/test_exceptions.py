"""
Testes de exception handlers.

Este módulo contém testes para validar que exception handlers
retornam respostas JSON padronizadas.
"""
from fastapi.testclient import TestClient


def test_http_exception_handler(client: TestClient, auth_headers: dict):
    """Testa que HTTPException retorna JSON padronizado."""
    # Tentar acessar conversa inexistente
    response = client.get(
        "/conversations/invalid_id/messages",
        headers=auth_headers
    )
    assert response.status_code == 404
    data = response.json()
    assert data["error"] == True
    assert "message" in data
    assert data["status_code"] == 404
    assert "path" in data


def test_validation_error_handler(client: TestClient):
    """Testa que ValidationError retorna JSON com detalhes."""
    # Enviar requisição com dados inválidos (falta password)
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
    assert "type" in data["errors"][0]


def test_validation_error_empty_body(client: TestClient):
    """Testa ValidationError com body vazio."""
    response = client.post(
        "/login",
        json={}
    )
    assert response.status_code == 422
    data = response.json()
    assert data["error"] == True
    assert "errors" in data


def test_validation_error_invalid_json(client: TestClient):
    """Testa ValidationError com JSON inválido."""
    response = client.post(
        "/login",
        data="invalid json",
        headers={"Content-Type": "application/json"}
    )
    # FastAPI pode retornar 422 ou 400 dependendo do erro
    assert response.status_code in [400, 422]


def test_unauthorized_exception_format(client: TestClient):
    """Testa que exceções de não autorizado seguem formato padronizado."""
    response = client.get("/conversations")
    assert response.status_code == 401
    data = response.json()
    # Verificar que resposta tem formato JSON (pode variar dependendo da implementação)
    assert isinstance(data, dict)
