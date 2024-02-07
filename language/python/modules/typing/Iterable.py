# It's an Object that can be iterated over, it's not necessarily a List

# %%
# str
my_str = "abc"
for el in my_str:
    print(el)


# %%
# list
my_list = ["a", "b", "c"]
for el in my_list:
    print(el)


# %%
# range
my_range = range(3)
for el in my_range:
    print(el)

# %%
# Accessing elements
foo = ["a", "b", "c", "d", ["e", "f"]]

foo[2]  # index 2
foo[4][0]  # nested index
foo[1:]  # from index 1 onwards
foo[:3]  # until index 3 (not inclusive)
foo[1:3]  # from index 1 until index 3 (not inclusive)
foo[-1]  # last index
# foo[::-1]  # reverse

# %%
# Overwriting elements (index must exist)
foo[0] = "z"  # index 0 is replaced
foo

# %%
# Removing elements
del foo[0]  # remove first element
foo
