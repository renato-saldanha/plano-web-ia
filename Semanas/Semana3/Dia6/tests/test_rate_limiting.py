"""
Script de teste de rate limiting
"""

from unittest.mock import AsyncMock, MagicMock, patch
from template import app


def test_chat_rate_limiting(client, auth_headers):
    """
    Testa rate limiting do chat-> 30/min
    """

    # Mock de resposta do LLM
    mock_ai_response = MagicMock()
    mock_ai_response.content = "Reposta mockada do LLM"

    # Mock do modelo ChatOpenAI
    mock_model = AsyncMock()
    mock_model.ainvoke = AsyncMock(return_value=mock_ai_response)

    with patch('template.ChatOpenAI', return_value=mock_model):
        conversation_id = None
        # Requisições válidas
        for i in range(30):
            if conversation_id:
                json = {
                    "message": f"Teste rate limiting chat {i+1}",
                    "conversation_id": conversation_id,
                    "stream": False,
                }
            else:
                json = {
                    "message": f"Teste rate limiting chat {i+1}",
                    "stream": False,
                }

            response1 = client.post(
                "/chat",
                headers=auth_headers,
                json=json
            )

            assert response1.status_code == 200 

            data = response1.json()
            assert "conversation_id" in data
            assert "reply" in data
            
            print(f"Teste rate limiting chat {i+1}")
            print(f"Conversation_id: {data["conversation_id"]}")
            print(f"Reply: {data["reply"]}")
            conversation_id = data["conversation_id"]
        

        # Requisição barrada
        response2 = client.post(
            "/chat",
            headers=auth_headers,
            json={
                "message": f"Teste rate limiting chat 31",
                "conversation_id": conversation_id,
                "stream": False,
            }
        )

        assert response2.status_code == 429

# Teste de login com cliente isolado
def test_login_rate_limiting(client, test_user):
    """
    Testa rate limiting do login-> 5/min
    """

    # Requisições válidas
    for i in range(5):
        response1 = client.post(
            "/login",
            json=test_user,
        )

    assert response1.status_code == 200

    # Requisição barrada
    response2 = client.post(
        "/login",
        json=test_user,
    )

    assert response2.status_code == 429
