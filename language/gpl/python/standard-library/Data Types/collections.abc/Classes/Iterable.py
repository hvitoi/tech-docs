# %%
from collections.abc import Iterable


# It's an Object that can be iterated over
# It must implement the method __iter__()

# list
foo: Iterable = ["a", "b", "c"]
for el in foo:
    print(el)

# string
foo: Iterable = "abc"
for el in foo:
    print(el)


# iterator
foo: Iterable = iter("abc")
for el in foo:
    print(el)
