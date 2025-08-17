# %%
from typing import Iterable

# Deprecated since Python 3.9! Use instead: collections.abc.Iterable


def print_iterable(elements: Iterable):
    for el in elements:
        print(el)


print_iterable(["a", "b", "c"])
print_iterable("abc")
print_iterable(range(3))
