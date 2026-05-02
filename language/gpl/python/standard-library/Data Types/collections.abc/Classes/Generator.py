# %%
from collections.abc import Generator
# In modern Python (3.5+), async/await largely replaced the use of full generators

# Generator is a more complex Iterator
# It additionally accepts .send(), .throw(), .close()


def infinite_counter() -> Generator[int]:
    n = 0
    while True:
        yield (n := n + 1)


it = infinite_counter()

next(it)
next(it)
next(it)
