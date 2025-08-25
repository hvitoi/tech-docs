# %%
from collections.abc import Iterable, Iterator

# It's am object that produces items one at a time
# Iterators are stateful, once exhausted, they cannot be reused
# It must implement the methods __iter__() and __next__()

numbers: Iterable = [1, 2, 3]
it: Iterator = iter(numbers)

for el in it:
    print(el)

# %%
# Iterator from yield syntax


def infinite_counter() -> Iterator:
    n = 0
    while True:
        yield (n := n + 1)


it: Iterator = infinite_counter()

next(it)
next(it)
next(it)
