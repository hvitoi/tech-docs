# %%
from unittest import TestCase
from functools import wraps


def fibonacci_with_array(n):
    """
    Time: O(n)
    Space: O(n)
    """
    fib = [0, 1]

    if n < 2:
        return fib[n]

    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib[-1]


def fibonacci_with_curr_prev(n):
    """
    Time: O(n)
    Space: O(1)
    """

    prev_prev = 0
    prev = 1
    curr = None

    if n == 0:
        return prev_prev

    if n == 1:
        return prev

    i = 2
    while i <= n:
        curr = prev + prev_prev
        prev_prev = prev
        prev = curr
        i += 1
    return curr


def fibonacci_recursive(n):
    """
    Time: O(2^n)
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_recursive_with_accumulator(n, acc=(0, 1)):
    """
    Time: O(n)
    """
    if n <= 1:
        return acc[n]

    return fibonacci_recursive_with_accumulator(
        n - 1,
        acc=(acc[1], acc[0] + acc[1]),
    )


def fibonacci_recursive_with_memoization(n, cache={}):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n - 1 not in cache:  # lookup or miss
        cache[n - 1] = fibonacci_recursive_with_memoization(n - 1, cache)

    if n - 2 not in cache:  # lookup or miss
        cache[n - 2] = fibonacci_recursive_with_memoization(n - 2, cache)

    return cache[n - 1] + cache[n - 2]


test_case = TestCase()

for fn in {
    fibonacci_with_array,
    fibonacci_with_curr_prev,
    fibonacci_recursive,
    fibonacci_recursive_with_accumulator,
    fibonacci_recursive_with_memoization,
}:
    test_case.assertEqual(fn(0), 0)
    test_case.assertEqual(fn(1), 1)
    test_case.assertEqual(fn(2), 1)
    test_case.assertEqual(fn(3), 2)
    test_case.assertEqual(fn(4), 3)
    test_case.assertEqual(fn(5), 5)

# %%
