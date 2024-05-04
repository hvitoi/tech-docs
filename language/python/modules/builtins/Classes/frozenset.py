# %%
# an immutable version of a set
# as it is immutable, it can be used as key for other conventional sets
my_frozen1 = frozenset(["a", "b", "c"])
my_frozen2 = frozenset(["a", "b", "c"])
my_frozen3 = frozenset(["d"])

set([my_frozen1, my_frozen2, my_frozen3])
