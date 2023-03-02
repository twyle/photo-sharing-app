def test_health(client):
    """Test the health check route."""
    test_response = client.get("/health")
    assert test_response.status_code == 200