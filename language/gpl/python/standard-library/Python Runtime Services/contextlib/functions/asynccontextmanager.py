## %%

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
