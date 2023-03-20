"""This module tests the password reset route."""


def test_password_reset_okay(client):
    """Test that a GET request returns a 200 response."""
    response = client.get("/auth/reset_password")
    assert response.status_code == 200
