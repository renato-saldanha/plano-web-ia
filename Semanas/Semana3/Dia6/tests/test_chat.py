"""
Testes de chat e histórico.

Este módulo contém testes para endpoints de chat:
- Criação de conversa
- Envio de mensagens
- Listagem de conversas
- Obtenção de mensagens
"""
from fastapi.testclient import TestClient


def test_create_conversation(client: TestClient, auth_headers: dict):
    """Testa criação de nova conversa via chat."""
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
    assert "user" in data


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
    assert all("created_at" in conv for conv in conversations)


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


def test_get_conversation_not_found(client: TestClient, auth_headers: dict):
    """Testa obtenção de mensagens de conversa inexistente."""
    response = client.get(
        "/conversations/invalid_id/messages",
        headers=auth_headers
    )
    assert response.status_code == 404
    data = response.json()
    assert data["error"] == True
    assert "não encontrada" in data["message"].lower()
