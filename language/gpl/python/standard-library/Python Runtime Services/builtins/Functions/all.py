# %%
all([True, 1, "a"])  # True
all([True, False])  # False
all([True, None])  # False

# %%
# equivalent to "every"
arr = [1, 1, 1, 1, 1]
all(el == 1 for el in arr)
