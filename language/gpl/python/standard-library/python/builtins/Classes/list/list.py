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

# Read

my_list = ["a", "b", "c"]
my_list[0]  # first
my_list[-1]  # last element
my_list[-3]  # first element

my_list[3]  # throws! (it does not exist)
my_list[-4]  # throws! (it does not exist)

# %%

# Write

my_list[-1] = "z"  # ["z", "b", "c"]
my_list[3] = "d"  # throws! This index does not exist, should be created first

# %%
# concatenate
["a", "b"] + ["c"]  # ["a", "b", "c"]
# ["a", "b"] + "c"  # fails!

# mutiply scalars
2 * ["a", "b"]  # ["a", "b", "a", "b"]

# multiply pointers (!!)
2 * [[]]  # [[], []] -- it's a reference to the same list!
[[] for _ in range(2)]  # use this instead


# %%
# list unpacking
l1 = ["a", "b"]

l1 + ["c"]
[*l1, "c"]  # same
