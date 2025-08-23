# %%

from unittest.mock import Mock

import httpx

# Build a response manually
client = httpx.Client()
client.get = Mock(
    return_value=httpx.Response(
        status_code=200,
        json={"foo": "bar"},
    )
)
client.get("https://example.com")
