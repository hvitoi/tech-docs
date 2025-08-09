# %%
any([True, 1, "a"])

# %%

# %%
any([True, False])

# %%
# equivalent to "some"
arr = [1, 1, 2, 1, 1]
any(el == 2 for el in arr)
