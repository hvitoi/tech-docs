# %%
from typing import Any, Iterator

it: Iterator[Any] = iter(("a", 1, True))

for el in it:
    print(el)
