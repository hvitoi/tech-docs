# %%
from collections.abc import Iterator
from typing import Any

it: Iterator[Any] = iter(("a", 1, True))
list(it)
