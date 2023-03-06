"""This module tests the registration route."""


def test_register_okay(client):
    """Test that a GET request returns a 200 response."""
    response = client.get("/auth/register")
    assert response.status_code == 200
