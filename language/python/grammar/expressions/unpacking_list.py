## Splat Operator
## The elements of a list/map are broken into individual elements
# Just like the spread operator (...) in javascript

# %%
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
list(zip(*matrix))  # transpose the matrix
# list(zip(matrix[0],matrix[1],matrix[2]))  # same


# %%
# concatenate arrays
a = [1, 2, 3]
b = [4, 5, 6]
[*a, *b]


# %%
# Unpack String
[*"abc"]
