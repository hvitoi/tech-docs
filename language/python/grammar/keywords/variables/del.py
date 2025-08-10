# unset/undefine a symbol!

# %%

# Plain variables
foo = "john"
del foo
# foo  # fails! (name 'foo' is not defined)

# %%

# Lists

# O(N) for the operation

# Just like pop() but does not return the popped value
foo = ["a", "b", "c"]
del foo[1]
foo  # ["a", "c"]

# %%

# Dicts
foo = {"a": 1, "b": 2, "c": 3}

del foo["a"]
foo

# %%
# Remove range of items
foo = ["a", "b", "c", "d", "e"]

del foo[1:-1]  # remove everything except first and last

foo
