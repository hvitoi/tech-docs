# %%
from unittest import TestCase


def is_even(num):
    return num % 2 == 0


test_case = TestCase()
test_case.assertFalse(is_even(7))
