# Similar to reduce, but returns a list instead with the ongoing results

# %%
from itertools import accumulate

it = accumulate([1, 2, 3, 4, 5], lambda acc, el: acc * el)
list(it)

# %%
it = accumulate([1, 2, 3, 4, 5], lambda acc, el: acc + el)
it = accumulate([1, 2, 3, 4, 5])  # same
list(it)
