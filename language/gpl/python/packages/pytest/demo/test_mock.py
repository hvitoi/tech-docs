from unittest.mock import patch


# Use unittest.mock.patch to replace an object during a test.
# pytest-mock provides a `mocker` fixture that wraps this with auto-cleanup.


def fetch_user(client, user_id):
    return client.get(f"/users/{user_id}").json()


class FakeClient:
    def get(self, path):
        raise RuntimeError("real network call")


def test_patch_method():
    client = FakeClient()
    with patch.object(FakeClient, "get") as mock_get:
        mock_get.return_value.json.return_value = {"id": 1, "name": "alice"}
        result = fetch_user(client, 1)

    assert result == {"id": 1, "name": "alice"}
    mock_get.assert_called_once_with("/users/1")
