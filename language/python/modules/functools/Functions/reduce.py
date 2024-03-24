# %%
from functools import reduce

reduce(lambda acc, el: acc + el, [1, 1, 1], 10)
reduce(lambda acc, el: acc + el, [1, 1, 1], 0)
reduce(lambda acc, el: acc + el, [1, 1, 1])
