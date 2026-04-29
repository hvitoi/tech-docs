# %%
import asyncio


async def do_something(name, delay):
    print(f"Coroutine {name} started")
    await asyncio.sleep(delay)
    print(f"Coroutine {name} finished")
    return f"{name} result"


async def main():
    # The coroutine is started right away. Even though it has not been awaited yet
    task = asyncio.create_task(do_something("A", 5))

    await asyncio.sleep(10)

    await task


if __name__ == "__main__":
    asyncio.run(main())
