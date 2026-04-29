# %%
import asyncio


# Async is not multi-threading, it's single-threaded cooperative multitasking
# Whenever this function is invoked, it's like it's executed on a new thread
# It works best when you have a lot of I/O-bound work (network, file, DB), not CPU-heavy tasks.
async def do_something(delay):
    print("Coroutine started")
    await asyncio.sleep(delay)
    print("Coroutine finished")
    return "Coroutine result"


async def main():
    # You can never use "await" outside an async def function
    await do_something(1)


if __name__ == "__main__":
    asyncio.run(main())  # you can't do "await main()"

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
