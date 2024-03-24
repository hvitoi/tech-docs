# %%
all([True, 1, "a"])

# %%
all([True, False])
all([True, None])

# %%
# equivalent to "every"
arr = [1, 1, 1, 1, 1]
all(el == 1 for el in arr)
