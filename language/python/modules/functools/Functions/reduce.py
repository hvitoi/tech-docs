# %%
from functools import reduce

reduce(lambda acc, el: acc + el, [1, 1, 1], 10)
reduce(lambda acc, el: acc + el, [1, 1, 1], 0)

# start = 0 is implicit
reduce(lambda acc, el: acc + el, [1, 1, 1])

# start = 1 is implicit
reduce(lambda acc, el: acc * el, [1, 1, 1])
