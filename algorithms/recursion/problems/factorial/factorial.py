# %%
from functools import reduce


def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_with_loop(n):
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    return fat


def factorial_recursive_with_accumulator(n, acc=1):
    if n == 0:
        return acc
    return factorial_recursive_with_accumulator(n - 1, acc * n)  # allows tail recursion


def factorial_reduce(n):
    if n == 0:
        return 1
    return reduce(
        lambda acc, el: acc * el,
        range(1, n + 1),
    )


for fn in {
    factorial_recursive,
    factorial_with_loop,
    factorial_recursive_with_accumulator,
    factorial_reduce,
}:
    assert fn(0) == 1
    assert fn(1) == 1
    assert fn(2) == 2
    assert fn(3) == 6
    assert fn(4) == 24
    assert fn(5) == 120
