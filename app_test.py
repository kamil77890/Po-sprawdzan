import pytest
from flask.testing import FlaskClient
from app import app, users

STATUS_OK = 200
CREATED = 201
NOT_FOUND = 404

@pytest.fixture
def client() -> FlaskClient:
    return app.test_client()

def test_ping(client: FlaskClient) -> None:
    expected_response = 'Pong!'
    actual = client.get('/ping')
    assert actual.data.decode('utf-8') == expected_response

def test_get_user_list(client: FlaskClient) -> None:
    actual = client.get('/users')
    assert actual.json == users
    assert actual.status_code == STATUS_OK

def test_get_user(client: FlaskClient) -> None:
    user_id = 1
    actual = client.get(f'/users/{user_id}')
    assert actual.json == users[user_id - 1]

def test_get_user_with_no_user(client: FlaskClient) -> None:
    user_id = len(users) + 2
    actual = client.get(f"/users/{user_id}")
    assert actual.status_code == NOT_FOUND

def test_create_user(client: FlaskClient) -> None:
    new_data = {"name": "pan", "lastname": "najleprzy_;)"}
    actual = client.post('/users', json=new_data)
    assert actual.status_code == CREATED

def test_update_user(client: FlaskClient) -> None:
    user_id = 1
    new_data = {"name": "Jane", "lastname": "Doe"}
    actual = client.patch(f"/users/{user_id}", json=new_data)
    assert actual.status_code == STATUS_OK

def test_delete_user(client: FlaskClient) -> None:
    user_id = 7
    actuall = client.delete(f"/users/{user_id}")
    assert actuall.status_code == STATUS_OK