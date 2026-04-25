# Similar to reduce, but returns a list instead with the ongoing results

# %%
import functools
import operator

functools.reduce(operator.mul, [1, 2, 3, 4, 5])
functools.reduce(lambda acc, el: acc * el, [1, 2, 3, 4, 5])  # same!
