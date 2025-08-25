# %%
import asyncio


# Async is not multi-threading, it's single-threaded cooperative multitasking
# Whenever this function is invoked, it's like it's executed on a new thread
# It works best when you have a lot of I/O-bound work (network, file, DB), not CPU-heavy tasks.
async def say_hello():
    print("Hello...")
    await asyncio.sleep(1)
    print("...world!")


async def main():
    # You can never use "await" outside an async def function
    await say_hello()


asyncio.run(main())

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
