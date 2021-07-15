import pytest
from hello import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data


def test_hello_github_actions(client):
    response = client.get('/github-actions')
    assert response.status_code == 200
    assert b'Hello, Github Actions!' in response.data


def test_hello_digital_ocean(client):
    response = client.get('/digital-ocean')
    assert response.status_code == 200
    assert b'Hello, Digital Ocean!' in response.data


def test_hello_linux(client):
    response = client.get('/linux')
    assert response.status_code == 200
