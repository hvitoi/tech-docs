# %%
# Tests if the two arguments point to the same object
True is True

# %%
l1 = []
l2 = []
l1 is l2  # False!

# %%
l1 = []
l2 = l1

l1 is l2  # True

# %%
l1 = []
l2 = l1[:]  # Shallow copy

l1 is l2  # False

# %%
l1 = [[], []]
l2 = l1[:]  # Shallow copy

l1[0] is l2[0]  # True!
