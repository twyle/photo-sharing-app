"""This module tests the login route."""


def test_login_okay(client):
    """Test that a GET request returns a 200 response."""
    response = client.get("/auth/login")
    assert response.status_code == 200
