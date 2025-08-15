# %%
# Concatenates 2 lists
my_list = ["a", "b", "c"]

my_list.extend(["d", "e", "f"])

my_list

# %%
a = ["a", "b", "c"]
b = ["d", "e", "f"]

[*a, *b]  # same output without mutation

# %%
a = ["a", "b", "c"]
b = ["d", "e", "f"]

a + b  # same output without mutation
