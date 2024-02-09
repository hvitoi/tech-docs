# O(N) for lists
# %%
# -> unset/undefine a symbol!

# plain variables
foo = "john"
del foo
# foo  # name is not defined

# lists
foo = ["a", "b", "c"]
del foo[1]
foo  # ["a", "c"]

# dict
foo = {
    "a": 1,
    "b": 2,
    "c": 3,
}

del foo["a"]
foo
