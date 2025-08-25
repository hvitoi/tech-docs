# %%

# GENEXPS
# Concept borrowed from Haskell
# Returns an iterator
# Syntax: <expression> for <item> in <iterable> if <condition>

from collections.abc import Generator
from typing import Iterable, Iterator

my_generator: Generator = (el for el in range(10))  # the pure form of the generator
isinstance(my_generator, Generator)  # True
isinstance(my_generator, Iterator)  # True, all generators are iterators
isinstance(my_generator, Iterable)  # True, all iterators are iterables
