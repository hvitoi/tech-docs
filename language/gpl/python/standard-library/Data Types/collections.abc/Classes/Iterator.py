# %%
from collections.abc import Iterable, Iterator  # Python 3.9+
# from typing import Iterator  # deprecated!

# It's an object that produces items one at a time
# Iterators are stateful, once exhausted, they cannot be reused
# It must implement the methods __iter__() and __next__()

numbers: Iterable = [1, 2, 3]
it: Iterator = iter(numbers)

for el in it:
    print(el)

# %%
# Iterator from yield syntax


def infinite_counter() -> Iterator[int]:
    """
    This is actually a generator, but since generators implement the Iterator interface so it can be casted
    """
    n = 0
    while True:
        yield (n := n + 1)


it = infinite_counter()

next(it)
next(it)
next(it)
