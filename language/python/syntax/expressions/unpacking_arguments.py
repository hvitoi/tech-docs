## Splat Operator
## The elements of a list/map are broken into individual elements
# Just like the spread operator (...) in javascript

# %%
def transpose(matrix):
    return list(zip(*matrix))
    # return list(zip(row1,row2,row3))  # same


transpose(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
)

# %%
# concatenate arrays
a = [1, 2, 3]
b = [4, 5, 6]
[*a, *b]


# %%
# Unpack Dict

from itertools import accumulate

my_map = {"initial": 10}
list(accumulate([1, 2, 3, 4, 5], **my_map))

# %%
# Unpack String
[*"abc"]
