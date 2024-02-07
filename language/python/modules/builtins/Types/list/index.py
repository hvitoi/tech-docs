# %%
my_list = ["a", "b", "z", "c", "z"]

# Get the first index of the element whose value is 'z'
my_list.index("z")

# %%
# Get the first found index starting from index 3 (inclusive)
my_list.index("z", 3)

# %%
# Get the first found index starting from index 3 (inclusive) and ending at index 4 (exclusive)
my_list.index("z", 3, 4)
