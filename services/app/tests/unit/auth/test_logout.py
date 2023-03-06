"""This module tests the logout route."""


def test_logout_okay(client):
    """Test that a GET request returns a 200 response."""
    response = client.get("/auth/logout")
    assert response.status_code == 307
