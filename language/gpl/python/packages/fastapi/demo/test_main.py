from fastapi.testclient import TestClient
from .main import app

# Follow the "test_*.py" naming convention


client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_headers():
    response = client.get(
        "/dependencies/deps5",
        headers={
            "X-Token": "fake-super-secret-token",
            "X-Key": "fake-super-secret-key",
        },
    )
    assert response.status_code == 200
    assert response.json() == "you are allowed"


def test_headers_bad_token():
    response = client.get(
        "/dependencies/deps5",
        headers={
            "X-Token": "fake-super-secret-token!",
            "X-Key": "fake-super-secret-key",
        },
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "X-Token header invalid"}


def test_read_nonexistent():
    response = client.get("/nonexistent-route")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


def test_create_item():
    response = client.post(
        "/models/user",
        json={
            "username": "henry",
            "full_name": "Henry Vitoi",
            "email": "henry@example.com",
            "password": "lala",
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "username": "henry",
        "full_name": "Henry Vitoi",
        "email": "henry@example.com",
    }
