# %%

# from literal
["a", 1, True, ["c", 9]]

# from dict
list({"b": 2, "a": 1})  # order is preserved, vals are discarded

# from str
list("abc")

# from tuple
list(("a", "b"))

# from another list (useful in functions in which you do not want to modify the original list)
my_list = ["a", "b"]
list(my_list)

# %%
# concatenate
["a", "b"] + ["c", "d"]  # ["a", "b", "c", "d"]

# mutiply scalars
2 * ["a", "b"]  # ["a", "b", "a", "b"]

# multiply pointers (!!)
2 * [[]]  # [[], []] -- it's a reference to the same list!
[[] for _ in range(2)]  # use this instead


# %%
# list unpacking
l1 = ["a", "b"]
[*l1]
