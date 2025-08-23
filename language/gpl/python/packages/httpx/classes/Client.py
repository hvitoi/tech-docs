# %%
import json

import httpx

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

# Client Options
with httpx.Client(base_url="https://httpbin.org/") as client:
    response = client.get("get")
    print(response.json())


# %%

# Stream response
with httpx.Client() as client:
    # client.stream() returns a 'httpx.Response' object
    with client.stream("GET", "https://httpbin.org/stream/5") as response:
        for chunk in response.iter_text():
            print(chunk)
