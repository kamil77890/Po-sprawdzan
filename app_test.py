import pytest
from flask.testing import FlaskClient
from app import app, users
import requests

STATUS_OK = 200
CREATED = 201
NOT_FOUND = 404

@pytest.fixture
def client() -> FlaskClient:
    return app.test_client()


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
    assert actual.status_code == 204

def test_delete_user(client: FlaskClient) -> None:
    user_id = 7
    actual = client.delete(f"/users/{user_id}")
    assert actual.status_code == 404


def test_integration(client: FlaskClient):
    actual = client.get('/users')
    assert actual.status_code == 200
    assert actual.json

    new_user_data = {"name": "John", "lastname": "Doe"}

    actual = client.post('/users', json=new_user_data)
    assert actual.status_code == 201

    new_user_id = actual.json.get("id")

    actual = client.get(f"/users/{new_user_id}")
    assert actual.status_code == 200
    assert actual.json["name"] == new_user_data["name"]
    assert actual.json["lastname"] == new_user_data["lastname"]

    updated_user_data = {"name": "jason", "lastname": "sołtys"}
    actual = client.patch(f"/users/{new_user_id}", json=updated_user_data)
    assert actual.status_code == 204

    actual = client.delete(f"/users/{new_user_id}")
    assert actual.status_code == 204

    actual = client.get(f"/users/{new_user_id}")
    assert actual.status_code == 404

if __name__ == "__main__":
    app.config['TESTING'] = True
    app.run("localhost", 8083)