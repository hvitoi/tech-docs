# %%
from collections.abc import Iterable


# It's an Object that can be iterated over, it's not necessarily a List
def print_iterable(elements: Iterable[str | int]):
    for el in elements:
        print(el)


print_iterable(["a", "b", "c"])
print_iterable("abc")
print_iterable(range(3))
