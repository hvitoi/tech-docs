# Unique unordered elements

# %%
# from literal
my_set = {1, 1, 2, 2, 3, 3, "a"}

# from list
my_set = set([1, 1, 2, 2, 3, 3])

# %%
# value need to be immutable elements because they will be hashed
my_set = {["a", "b"]}  # fails!

# %%
# difference
{"a", "b"} - {"b"}

# %%
# Empty set
set()
{*()}  # same, overly verbose
{}  # it's not a set! It's a dict!
