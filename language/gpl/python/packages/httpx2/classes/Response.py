# %%

from unittest.mock import Mock

from httpx2 import Client, Response

# Build a response manually
client = Client()
client.get = Mock(
    return_value=Response(
        status_code=200,
        json={"foo": "bar"},
    )
)
client.get("https://example.com")
