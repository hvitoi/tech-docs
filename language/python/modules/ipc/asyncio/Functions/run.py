import asyncio


# Async is not multi-threading, it's single-threaded cooperative multitasking
# Whenever this function is invoked, it "like" is executed on a new thread
# It works best when you have a lot of I/O-bound work (network, file, DB), not CPU-heavy tasks.
async def say_hello():
    print("Hello...")
    await asyncio.sleep(1)  # Pause the local thread
    print("...world!")


async def main():
    # You can never use "await" outside an async def function
    await say_hello()


asyncio.run(main())
