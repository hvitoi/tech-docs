# %%
from typing import Iterator

# Deprecated since Python 3.9! Use instead: collections.abc.Iterator

it: Iterator[str] = iter(("a", "b", "c"))
list(it)
