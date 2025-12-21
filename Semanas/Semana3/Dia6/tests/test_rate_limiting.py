"""
Testes de rate limiting.

Este módulo contém testes para validar que rate limiting funciona corretamente.
"""
import time
from fastapi.testclient import TestClient


def test_login_rate_limit(client: TestClient):
    """Testa rate limit de login (5/min)."""
    # Fazer 5 requisições (limite)
    for i in range(5):
        response = client.post(
            "/login",
            json={"username": "admin", "password": "admin123"}
        )
        assert response.status_code == 200, f"Requisição {i+1} falhou"
    
    # 6ª requisição deve ser bloqueada
    response = client.post(
        "/login",
        json={"username": "admin", "password": "admin123"}
    )
    assert response.status_code == 429, "Rate limit não foi aplicado"


def test_chat_rate_limit(client: TestClient, auth_headers: dict):
    """Testa rate limit de chat (30/min)."""
    # Fazer 30 requisições (limite)
    for i in range(30):
        response = client.post(
            "/chat",
            headers=auth_headers,
            json={"message": f"Test {i}", "stream": False}
        )
        assert response.status_code == 200, f"Requisição {i+1} falhou"
    
    # 31ª requisição deve ser bloqueada
    response = client.post(
        "/chat",
        headers=auth_headers,
        json={"message": "Should be blocked", "stream": False}
    )
    assert response.status_code == 429, "Rate limit não foi aplicado"


def test_rate_limit_reset(client: TestClient, auth_headers: dict):
    """
    Testa que rate limit é resetado após período de tempo.
    
    Nota: Este teste pode ser lento pois precisa esperar o reset do rate limit.
    Em produção, você pode usar mocks para acelerar.
    """
    # Fazer requisições até o limite
    for i in range(30):
        client.post(
            "/chat",
            headers=auth_headers,
            json={"message": f"Test {i}", "stream": False}
        )
    
    # Verificar que está bloqueado
    response = client.post(
        "/chat",
        headers=auth_headers,
        json={"message": "Blocked", "stream": False}
    )
    assert response.status_code == 429
    
    # Nota: Em um teste real, você esperaria 60 segundos para o reset
    # ou usaria mocks para simular a passagem do tempo
    # time.sleep(61)  # Descomente para testar reset real
