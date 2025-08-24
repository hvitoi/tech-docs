# %%
# Take one element of each Iterable in order and put then together in a tuple
# Finishes as the shortest Iterable is exhausted


arr1 = "abc"
arr2 = [1, 2, 3, 4]  # 4 is ignored
list(zip(arr1, arr2))

# %%
# Transpose matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

list(zip(*matrix))
