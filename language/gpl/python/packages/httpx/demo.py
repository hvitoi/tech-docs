# %%
import asyncio
import json
from unittest.mock import Mock

import httpx


# %%
# ---- Asynchronous example ----
async def do_req_async():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://httpbin.org/get")
        print("Response Status:", response.status_code)
        print("Response Body:", json.dumps(response.json(), indent=4))


if __name__ == "__main__":
    # Doesn't work from inside a Jupyter notebook
    asyncio.run(do_req_async())

# %%
# ---- Synchronous example ----
with httpx.Client() as client:
    response = client.post(
        "https://httpbin.org/post",
        json={"foo": "bar"},  # for application/json
        # data={"foo": "bar"}, # for application/x-www-form-urlencoded
        params={"limit": 999},  # query parameters
        headers={"Foo-Foo": "bar"},
        cookies={"session": "abc123"},  # Cookie header
        auth=httpx.BasicAuth("user", "pass"),  # Authorization Basic Header
        timeout=5.0,
    )

    print("Response Status:", response.status_code)
    print("Response Body:", json.dumps(response.json(), indent=4))
    print("Response Headers:", response.headers)


# %%

# Stream response
with httpx.Client() as client:
    # client.stream() returns a 'httpx.Response' object
    with client.stream("GET", "https://httpbin.org/stream/5") as response:
        for chunk in response.iter_text():
            print(chunk)

# %%
# Build a response manually
client = httpx.Client()
client.get = Mock(
    return_value=httpx.Response(
        status_code=200,
        json={"foo": "bar"},
    )
)
client.get("https://example.com")
