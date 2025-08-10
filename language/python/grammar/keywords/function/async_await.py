# %%
import asyncio


async def do_something(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished")


async def main():
    # Run both at the same time
    await asyncio.gather(
        do_something("A", 2),
        do_something("B", 1),
    )


asyncio.run(main())
