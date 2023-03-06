"""This module tests the password reset route."""


def test_reset_request_okay(client):
    """Test that a GET request returns a 200 response."""
    response = client.get("/auth/reset_request")
    assert response.status_code == 200
