# %%
import asyncio

# Async Functions (Coroutines)


# "coroutine" is the object return by calling an async function
# Python knows that it is something like a function, that it can start and that it will end at some point, but that it might be paused internally too, whenever there is an await inside of it.


async def do_something(name, delay):
    print(f"Coroutine {name} started")
    await asyncio.sleep(delay)
    print(f"Coroutine {name} finished")
    return "foo"


async def main():
    # The coroutine is NOT started yet. It will only start when it is awaited
    coroutine = do_something("A", 5)

    # Start the coroutine, block the program until it returns the result
    print(await coroutine)


if __name__ == "__main__":
    asyncio.run(main())


# %%


# When a async def function uses "yield" it returns no more a coroutine, but rather an AsyncIterator is created
async def counter(max):
    n = 0
    while n < max:
        await asyncio.sleep(1)
        yield (n := n + 1)


async def main():
    ait = counter(5)
    async for el in ait:
        print(el)


if __name__ == "__main__":
    asyncio.run(main())
