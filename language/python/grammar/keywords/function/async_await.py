# %%
import asyncio


## asynchronous code uses "coroutines", with async and await syntax.
## "coroutine" is the outside of "async def" function - Python knows that it is something like a function, that it can start and that it will end at some point, but that it might be paused internally too, whenever there is an await inside of it.


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
