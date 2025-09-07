from unittest.mock import AsyncMock

import httpx
from fastapi.testclient import TestClient

from app.features.dependency_httpx import get_http_client
from app.main import app

# Follow the "test_*.py" naming convention
# "pytest -vv to run it"


http_client = TestClient(app)


def test_read_root():
    response = http_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_headers():
    response = http_client.get(
        "/dependencies/deps5",
        headers={
            "X-Token": "fake-super-secret-token",
            "X-Key": "fake-super-secret-key",
        },
    )
    assert response.status_code == 200
    assert response.json() == "you are allowed"


def test_headers_bad_token():
    response = http_client.get(
        "/dependencies/deps5",
        headers={
            "X-Token": "fake-super-secret-token!",
            "X-Key": "fake-super-secret-key",
        },
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "X-Token header invalid"}


def test_read_nonexistent():
    response = http_client.get("/nonexistent-route")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


def test_create_item():
    response = http_client.post(
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


## --- client.websocket_connect

# def test_websocket():
#     with client.websocket_connect("websockets/ws") as websocket:
#         data = websocket.receive_json()
#         assert data == {"msg": "Hello WebSocket"}


## --- dependency_overrides (mocks)


async def fake_get_http_client():
    client = httpx.AsyncClient()
    client.get = AsyncMock(
        return_value=httpx.Response(
            status_code=200,
            json={"foo": "bar"},
        )
    )
    return client


app.dependency_overrides[get_http_client] = fake_get_http_client


def test_httpx_request():
    response = http_client.get(
        "/dependency_httpx/repo_stat",
        params={"repo": "fake/repo"},
    )
    assert response.status_code == 200
    assert response.json() == {"foo": "bar"}


app.dependency_overrides = {}  # reset to original functions
