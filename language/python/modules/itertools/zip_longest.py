# %%
import itertools
from typing import Iterator, Any

# Takes one element from each Iterable object and creates a tuple out of it
# fillvalue is used whenever one of the Iterables has already been exhausted (defaults to None)
it: Iterator[Any] = itertools.zip_longest("ABCD", "xy", fillvalue="")

for el in it:
    print(el)
