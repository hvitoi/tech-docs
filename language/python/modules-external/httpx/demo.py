# %%
import httpx
import asyncio


# %%
# ---- Synchronous example ----
def sync_example():
    with httpx.Client() as client:
        response = client.get("https://httpbin.org/get", params={"q": "hello"})
        print("Status:", response.status_code)
        print("Body:", response.json())


if __name__ == "__main__":
    sync_example()


# %%
# ---- Asynchronous example ----
async def async_example():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://httpbin.org/get", params={"q": "hello"})
        print("Status:", response.status_code)
        print("Body:", response.json())


if __name__ == "__main__":
    # Doesn't work from inside a Jupyter notebook
    asyncio.run(async_example())
