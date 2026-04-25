# %%
import functools

functools.reduce(lambda acc, el: acc + el, [1, 1, 1], 10)
functools.reduce(lambda acc, el: acc + el, [1, 1, 1], 0)

# start = 0 is implicit
functools.reduce(lambda acc, el: acc + el, [1, 1, 1])

# start = 1 is implicit
functools.reduce(lambda acc, el: acc * el, [1, 1, 1])
