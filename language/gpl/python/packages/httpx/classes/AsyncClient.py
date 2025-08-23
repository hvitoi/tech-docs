# %%
import asyncio
import json

import httpx


async def do_req_async():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://httpbin.org/get")
        print("Response Status:", response.status_code)
        print("Response Body:", json.dumps(response.json(), indent=4))


if __name__ == "__main__":
    # Doesn't work from inside a Jupyter notebook
    asyncio.run(do_req_async())
