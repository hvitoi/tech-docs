# %%
import asyncio
from collections.abc import AsyncIterable, AsyncIterator

# It must implement the methods __aiter__() and __anext__()


async def counter(max: int) -> AsyncIterator:
    n = 0
    while n < max:
        await asyncio.sleep(1)
        yield (n := n + 1)


async def main():
    # Async for
    ait: AsyncIterable = counter(5)
    async for el in ait:
        print(el)

    # Async list comprehension
    [el async for el in counter(5)]


if __name__ == "__main__":
    asyncio.run(main())
