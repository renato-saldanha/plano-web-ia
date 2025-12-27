
def test_health(client):
    """
    Health check
    """
    response = client.get("/health")
    assert response.status_code == 200

