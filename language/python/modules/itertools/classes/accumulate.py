# Similar to reduce, but returns a list instead with the ongoing results

# %%
import itertools

it = itertools.accumulate([1, 2, 3, 4, 5], lambda acc, el: acc * el)
list(it)

# %%
it = itertools.accumulate([1, 2, 3, 4, 5], lambda acc, el: acc + el)
it = itertools.accumulate([1, 2, 3, 4, 5])  # same
list(it)


# %%
# Accumulator step by step
def accumulator(acc, el):
    print(acc, el)
    return acc + el


it = itertools.accumulate([1, 2, 3, 4, 5], accumulator)
list(it)


# %%
# with initial value a new element is added to the beginning of the list
it = itertools.accumulate([1, 2, 3, 4, 5], accumulator, initial=0)  # with initial value
list(it)
