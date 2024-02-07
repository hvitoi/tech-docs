# %%
from functools import reduce

reduce(lambda acc, el: acc * el, [1, 2, 3, 4, 5], 1)
