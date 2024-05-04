# %%
my_list = ["a", 1, True, ["c", 9]]
my_list

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

# multiply pointers (!!)
# watch out! It's reference to the same list
2 * [[]]  # [[], []]
[[] for _ in range(2)]  # use this instead

# %%
# from dict
list({"b": 2, "a": 1})  # order is preserved, vals are discarded

# %%
# from str
list("abc")

# %%
# from tuple
list(("a", "b"))  # values are flattened
