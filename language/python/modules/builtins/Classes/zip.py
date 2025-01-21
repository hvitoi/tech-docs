# %%
# Take each element at same position and put together a a tuple
# Finishes as the shortest Iterable is exhausted

arr1 = "abc"
arr2 = [1, 2, 3, 4]
list(zip(arr1, arr2))

# %%
# Transpose matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

list(zip(*matrix))
