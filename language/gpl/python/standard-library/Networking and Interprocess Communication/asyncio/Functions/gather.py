import asyncio


async def do_something(name, delay):
    """
    When invoked, it returns a coroutine! No actual execution, execution is performed only when it is awaited
    """
    print(f"Coroutine {name} started")
    await asyncio.sleep(delay)
    print(f"Coroutine {name} finished")
    return f"{name} result"


async def main():
    coroutines = [
        do_something("A", 3),
        do_something("B", 2),
    ]

    # The coroutines start at this point! (the same wouldn't happen if you just created the 2 coros independently)
    tasks = asyncio.gather(*coroutines, return_exceptions=True)

    # Other coroutines outside of the gather
    await do_something("C", 1)

    # As the coros were already running in the background, here they will return instantly
    results = await tasks
    print(f"Final result: {results}")


if __name__ == "__main__":
    asyncio.run(main())
