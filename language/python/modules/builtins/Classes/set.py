# %%
# Unique unordered elements
my_set = {1, 1, 2, 2, 3, 3}
my_set

# %%
# value need to be immutable elements because they will be hashed
my_set = {["a", "b"]}  # fails!

# %%
# difference
{"a", "b"} - {"b"}


# %%
# from list
my_set = set([1, 1, 2, 2, 3, 3])
my_set

# %%
# Empty set
{*()}
set()  # same
{}  # it's a dict!
