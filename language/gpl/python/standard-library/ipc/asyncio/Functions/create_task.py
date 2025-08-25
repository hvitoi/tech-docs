# %%
import asyncio


async def just_wait(delay):
    print("Coroutine started")
    await asyncio.sleep(delay)
    print("Coroutine finished")


async def main():
    # The coroutine is started right away. Even though it has not been awaited yet
    coroutine = asyncio.create_task(just_wait(5))

    await asyncio.sleep(10)

    await coroutine


if __name__ == "__main__":
    asyncio.run(main())
