# Similar to reduce, but returns a list instead with the ongoing results

# %%
from itertools import accumulate

it = accumulate([1, 2, 3, 4, 5], lambda acc, el: acc * el)
list(it)

# %%
it = accumulate([1, 2, 3, 4, 5], lambda acc, el: acc + el)
it = accumulate([1, 2, 3, 4, 5])  # same
list(it)


# %%
# Accumulator step by step
def accumulator(acc, el):
    print(acc, el)
    return acc + el


it = accumulate([1, 2, 3, 4, 5], accumulator)
list(it)


# %%
# with initial value a new element is added to the beginning of the list
it = accumulate([1, 2, 3, 4, 5], accumulator, initial=0)  # with initial value
list(it)
