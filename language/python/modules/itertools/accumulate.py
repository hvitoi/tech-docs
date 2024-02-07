# Similar to reduce, but returns a list instead with the ongoing results

# %%
from itertools import accumulate

list(accumulate([1, 2, 3, 4, 5], lambda acc, el: acc * el))
