import asyncio


async def task(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished")


async def main():
    # Run both at the same time
    await asyncio.gather(
        task("A", 2),
        task("B", 1),
    )


asyncio.run(main())
