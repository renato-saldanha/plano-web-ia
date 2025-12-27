"""
Script de teste de chat
"""

from requests import auth


def test_create_conversation(client, auth_headers):
    """
    Testa a criação de um chat
    """

    response = client.post(
        "/chat",
        headers=auth_headers,
        json={
            "message": "Olá, como vai?",
            "stream": False,
        })

    assert response.status_code == 200
    data = response.json()
    assert "conversation_id" in data
    assert "reply" in data


def test_send_message_with_exists_conversation(client, auth_headers):
    """
    Testa o envio de mensagem em uma conversa existente
    """

    response1 = client.post(
        "/chat",
        headers=auth_headers,
        json={
            "message": "Olá, como vai?",
            "stream": False,
        })

    conversation_id = response1.json()["conversation_id"]

    response2 = client.post(
        "/chat",
        headers=auth_headers,
        json={
            "message": "Teste conversa existente",
            "conversation_id": conversation_id,
            "stream": False,
        }
    )

    assert response2.status_code == 200
    data = response2.json()
    assert "conversation_id" in data
    assert "reply" in data


def test_list_conversation(client, auth_headers):
    """
    Testa a listagem de uma conversa.
    """

    for i in range(3):
        response = client.post(
            "/chat",
            headers=auth_headers,
            json={
                "message": f"Mensagem teste {i}",
                "stream": False,
            }
        )

    response = client.get("/conversations", headers=auth_headers)

    assert response.status_code == 200
    conversations = response.json()

    assert len(conversations) == 3
    assert all("id" in conv for conv in conversations)
    assert all("message_count" in conv for conv in conversations)


def test_get_messages_by_conversation_id(client, auth_headers):
    """
    Testa a listagem de mensagens de uma conversa.
    """

    response1 = client.post(
        "/chat",
        headers=auth_headers,
        json={
            "message": f"Teste lista mensagens 1",
            "stream": False,
        }
    )

    conversation_id1 = response1.json()["conversation_id"]

    response2 = client.post(
        "/chat",
        headers=auth_headers,
        json={
            "message": f"Teste lista mensagens 2",
            "conversation_id": conversation_id1,
            "stream": False,
        }
    )

    conversation_id = response2.json()["conversation_id"]  

    response3 = client.get(
        f"/conversations/{conversation_id}/messages",
        headers=auth_headers,
    )

    assert response3.status_code == 200
    messages = response3.json()
    assert len(messages) == 4
    assert messages[0]["role"] == "user"
    assert messages[1]["role"] == "assistant"
