# %%
import asyncio
from collections.abc import AsyncIterator, AsyncIterable

# It must implement the method __aiter__()


async def counter(max: int) -> AsyncIterator:
    n = 0
    while n < max:
        await asyncio.sleep(1)
        yield (n := n + 1)


async def main():
    ait: AsyncIterable = counter(5)
    async for el in ait:
        print(el)


if __name__ == "__main__":
    asyncio.run(main())
