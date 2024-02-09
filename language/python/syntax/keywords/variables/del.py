# O(N) for lists
# %%
# -> unset/undefine a symbol!

# plain variables
foo = "john"
del foo
# foo  # name is not defined

# %%
# lists

# Just like pop() but does not return the popped value
foo = ["a", "b", "c"]
del foo[1]
foo  # ["a", "c"]

# %%
# dict
foo = {"a": 1, "b": 2, "c": 3}

del foo["a"]
foo

# %%
# Remove range of items
foo = ["a", "b", "c", "d", "e"]

del foo[1:-1]  # remove everything except first and last

foo
