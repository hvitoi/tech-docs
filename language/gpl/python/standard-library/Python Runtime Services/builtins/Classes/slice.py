# Returns a slice object

# %%
my_list = ["a", "b", "c", "d", "e"]
my_list[slice(3)]  # Until index 2 (exclusive)
my_list[:3]  # same

# %%
my_list = ["a", "b", "c", "d", "e"]
my_list[slice(1, 3)]  # From index 1 (inclusive) until index 2 (exclusive)
my_list[1:3]  # same

# %%
my_list = ["a", "b", "c", "d", "e"]
my_list[slice(None, None, -1)]  # Reversed
my_list[::-1]  # same
