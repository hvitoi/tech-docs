# %%
import itertools

# Creates 5 groups
it = itertools.groupby(
    [1, 2, 3, 4, 5],
    lambda el: el % 2 == 0,
)

# Creates 2 groups
it = itertools.groupby(
    [1, 3, 5, 2, 4],
    lambda el: el % 2 == 0,
)

list(it)
