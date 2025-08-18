# %%
import functools


def divide(dividend, divisor):
    return dividend / divisor


# if kwargs is not defined, it will always replace the left-most arg
divide_by_2 = functools.partial(divide, divisor=2)
divide_by_2(10)
