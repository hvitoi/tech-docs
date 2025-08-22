# %%
import asyncio


# asynchronous code uses "coroutines", with async and await syntax.
# "coroutine" is the object return by calling an async function
# Python knows that it is something like a function, that it can start and that it will end at some point, but that it might be paused internally too, whenever there is an await inside of it.


async def do_something(name, delay):
    print(f"Coroutine {name} started")
    await asyncio.sleep(delay)
    print(f"Courtine {name} finished")
    return "foo"


async def main():
    # Run both at the same time
    # At this point the async function is executed, but it does not block the program
    coroutines = asyncio.gather(
        do_something("A", 2),
        do_something("B", 1),
    )

    # Block the program and wait for the result of the coroutines
    results = await coroutines

    print(results)


asyncio.run(main())
