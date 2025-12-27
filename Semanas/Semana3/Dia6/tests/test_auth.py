def test_login_success(client, test_user):
    """
    Teste de login com credenciais válidas.
    """

    response = client.post("/login", json=test_user)

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data


def test_login_invalid_username(client, test_user_invalid_username):
    """
    Teste para validar um login feito com usuário errado.
    """

    response = client.post("/login", json=test_user_invalid_username)

    assert response.status_code == 401
    assert "Usuário inválido." in response.json()["message"]


def test_login_invalid_password(client, test_user_invalid_password):
    """
    Teste para validar um login feito com usuário errado.
    """

    response = client.post("/login", json=test_user_invalid_password)

    assert response.status_code == 401
    assert "Senha inválida." in response.json()["message"]


def test_protected_route_without_token(client, test_user):
    """
    Testa acesso a uma rota protegida sem token
    """

    response = client.get("/conversations")
    assert response.status_code == 401


def test_protected_route_with_invalid_token(client):
    """
    Testa acesso a uma rota protegida com token inválido
    """
    headers = {"Authorization": "Bearer invalid"}
    response = client.get("/conversations", headers=headers)
    assert response.status_code == 401


def test_protected_route_with_valid_token(client, auth_headers):
    """
    Testa acesso a uma rota protegida com token valido.
    """

    response = client.get("/conversations", headers=auth_headers)
    assert response.status_code == 200