# O(N)
# %%
# maximum between two values
max(4, 6)
max([1, 2, 3])

# %%
# Choose key
max([("y", 2), ("z", 1), ("x", 3)])  # takes the first key by default
max(
    [("y", 2), ("z", 1), ("x", 3)], key=lambda el: el[1]
)  # specify how to retrieve the key
