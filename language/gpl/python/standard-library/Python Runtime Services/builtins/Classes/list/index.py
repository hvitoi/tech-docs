# %%
# Get the first index of a matching element

my_list = ["a", "b", "z", "c", "z"]

my_list.index("z")  # index 2

# %%
my_list = ["a", "b", "c"]
my_list.index("z")  # Throws!

# %%
# Get the first found index starting from index 3 (inclusive)
my_list = ["a", "b", "z", "c", "z"]
my_list.index("z", 3)

# %%
# Get the first found index starting from index 3 (inclusive) and ending at index 4 (exclusive)
my_list = ["a", "b", "z", "c", "z"]
my_list.index("z", 3, 5)
