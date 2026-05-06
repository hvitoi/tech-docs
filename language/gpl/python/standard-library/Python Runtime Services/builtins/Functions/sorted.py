# %%
arr = [2, 3, 1, 5, 4]

sorted(arr)
sorted(arr, reverse=True)

# %%
# get the key for ordering
arr = [{"id": 3}, {"id": 1}, {"id": 2}]

sorted(arr, key=lambda el: el["id"])
