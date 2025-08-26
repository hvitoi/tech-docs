# %%
any([True, False])  # True
any(["foo", False])  # True
any([False, False])  # False

# %%
# equivalent to "some"
arr = [1, 1, 2, 1, 1]
any(el == 2 for el in arr)
