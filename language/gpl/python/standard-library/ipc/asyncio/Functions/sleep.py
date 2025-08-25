import asyncio

# It suspends only the current coroutine and gives control back to the event loop
# It's like an await on nothing


async def say_hello():
    print("Hello...")
    await asyncio.sleep(1)
    print("...world!")


async def main():
    await say_hello()


asyncio.run(main())
