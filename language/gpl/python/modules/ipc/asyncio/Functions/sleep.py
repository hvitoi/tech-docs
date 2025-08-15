import asyncio


async def say_hello():
    print("Hello...")
    await asyncio.sleep(1)  # Pause the local thread
    print("...world!")


async def main():
    await say_hello()


asyncio.run(main())
