# %%
from collections.abc import Generator


# Generator is a "simpler" Iterator. It doesn't accept ".send"


def infinite_counter() -> Generator:
    n = 0
    while True:
        yield (n := n + 1)


it = infinite_counter()

next(it)
next(it)
next(it)
