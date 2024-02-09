## Splat Operator
## The elements of a list/map are broken into individual elements

# %%
# Unpack List

# Just like the spread operator (...) in javascript
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

list(zip(*matrix))

# same as:
list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))

# put it back in a list
[*matrix]

# %%
# Unpack Dict

from itertools import accumulate

my_map = {"initial": 10}
list(accumulate([1, 2, 3, 4, 5], **my_map))
