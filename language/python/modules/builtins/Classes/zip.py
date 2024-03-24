# %%

# Take each element at same position and put together a a tuple
# Finishes as the shortest Iterable is exhausted

list(zip("abc", [1, 2, 3, 4]))

# %%
# Transpose matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

list(zip(*matrix))
