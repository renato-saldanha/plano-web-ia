"""
Testes de autenticação.

Este módulo contém testes para endpoints de autenticação:
- Login
- Refresh token
- Proteção de rotas
"""
from fastapi.testclient import TestClient


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


def test_login_invalid_username(client: TestClient):
    """Testa login com usuário inválido."""
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
    data = response.json()
    assert data["error"] == True
    assert "Senha inválida" in data["message"]


def test_refresh_token_success(client: TestClient):
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
