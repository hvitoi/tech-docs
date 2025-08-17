# %%

# from literal
my_list = ["a", 1, True, ["c", 9]]

# from dict
list({"b": 2, "a": 1})  # order is preserved, vals are discarded

# from str
list("abc")

# from tuple
list(("a", "b"))

# %%
my_list = []
if my_list:
    print("I won't print")

# %%
# concatenate lists
["a", "b"] + ["c", "d"]

# %%
# multiply scalars
2 * ["a", "b"]  # ["a", "b", "a", "b"]

# %%
# multiply pointers (!!)
# watch out! It's reference to the same list
2 * [[]]  # [[], []]
[[] for _ in range(2)]  # use this instead


# %%
l1 = ["a", "b"]
l2 = ["c", "d"]
l3 = ["e", "f"]

l1 + l2 + [*l3]

# %%
# from another list
my_list = ["a", "b"]

# useful in functions in which you do not want to modify the original list
another_list = list(my_list)
