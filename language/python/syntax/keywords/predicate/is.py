# %%
# Tests if the two arguments point to the same object
True is True

# %%
[] is []  # False!

# %%
foo1 = []
foo2 = foo1

foo1 is foo2  # True

# %%
foo1 = []
foo2 = foo1[:]  # Shallow copy

foo1 is foo2  # False

# %%
foo1 = [[], []]
foo2 = foo1[:]  # Shallow copy

foo1[0] is foo2[0]  # True!
