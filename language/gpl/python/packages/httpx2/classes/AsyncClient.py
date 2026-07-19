# %%
import asyncio
import json

from httpx2 import AsyncClient


async def do_req_async():
    async with AsyncClient() as client:
        response = await client.get("https://httpbin.org/get")
        print("Response Status:", response.status_code)
        print("Response Body:", json.dumps(response.json(), indent=4))


if __name__ == "__main__":
    # Doesn't work from inside a Jupyter notebook
    asyncio.run(do_req_async())
