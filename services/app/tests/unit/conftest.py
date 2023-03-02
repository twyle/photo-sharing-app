import pytest
from api import create_app


@pytest.fixture()
def test_app():
    app = create_app()
    with app.app_context():
        yield app


@pytest.fixture()
def client(test_app):
    return test_app.test_client()
