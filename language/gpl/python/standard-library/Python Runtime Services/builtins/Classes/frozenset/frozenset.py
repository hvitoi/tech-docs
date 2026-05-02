# %%
# an immutable version of a set
# as it is immutable, it can be used as key for other conventional sets
my_frozen1 = frozenset(["a", "b", "c"])
my_frozen2 = frozenset(["a", "b", "c"])
my_frozen3 = frozenset(["d"])

set([my_frozen1, my_frozen2, my_frozen3])

# %%
# The order of the elements doesn't matter, frozenset will order it
assert frozenset({"a": 1, "b": 2}) == frozenset({"a": 1, "b": 2})
assert frozenset({"a": 1, "b": 2}) == frozenset({"b": 2, "a": 1})
assert frozenset(("a", "b")) == frozenset(("a", "b"))
assert frozenset(("a", "b")) == frozenset(("b", "a"))
