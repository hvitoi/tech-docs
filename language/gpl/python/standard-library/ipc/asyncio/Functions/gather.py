import asyncio


async def task(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished")


async def main():
    # The coroutines are started at this point! (the same wouldn't happen if you just created the 2 coros independently)
    tasks = [
        task("A", 4),
        task("B", 3),
    ]
    coroutines = asyncio.gather(*tasks, return_exceptions=True)

    await asyncio.sleep(10)  # the tasks are already running while this is sleeping

    # As the coros were already running in the background, here they will return instantly
    await coroutines


asyncio.run(main())
