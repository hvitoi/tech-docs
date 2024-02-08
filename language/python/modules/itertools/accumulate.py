# Similar to reduce, but returns a list instead with the ongoing results

# %%
import itertools

it = itertools.accumulate([1, 2, 3, 4, 5], lambda acc, el: acc * el)
it = itertools.accumulate([1, 2, 3, 4, 5])  # same

list(it)
