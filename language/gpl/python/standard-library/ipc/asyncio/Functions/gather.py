import asyncio


async def task(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished")


async def main():
    # The coroutines are started at this point! (the same wouldn't happen if you just created the 2 coros independently)
    coroutines = asyncio.gather(
        task("A", 2),
        task("B", 1),
    )

    await asyncio.sleep(10)

    # As the coros were already running in the background, here they will return instantly
    await coroutines


asyncio.run(main())
