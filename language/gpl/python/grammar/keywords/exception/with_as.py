# %%
# It's used when working with unmanaged resources (like file streams).
# Ensures that the resource is gracefully closed even if exceptions are thrown
# It's syntactic sugar for try/finally blocks.

# The expression must be an object that supports the "context management protocol"
# The "context management protocol" has the methods __enter__() and __exit__()

# %%
# ---- File open ----
# open() creates a  an object that is called a "Context Manager"
with open("file.txt") as file_content:
    for line in file_content:
        print(line)

# same as:
file_content = open("file.txt")
for line in file_content:
    print(line)

# %%
# ---- HTTP request ---
import httpx

with httpx.Client() as client:
    response = client.get("https://httpbin.org/get")
    print("Status:", response.status_code)
    print("Body:", response.json())

# %%


import asyncio
from contextlib import asynccontextmanager


# create a function that implements the "context management protocol"
@asynccontextmanager
async def connect_to_service():
    print("🔌 Connecting to service...")
    await asyncio.sleep(1)  # simulate async setup
    try:
        yield "connection-object"
    finally:
        print("❌ Closing connection...")
        await asyncio.sleep(1)  # simulate async cleanup


async def main():
    async with connect_to_service() as conn:
        print(f"✅ Using {conn}")
        await asyncio.sleep(2)  # simulate doing some work


asyncio.run(main())
