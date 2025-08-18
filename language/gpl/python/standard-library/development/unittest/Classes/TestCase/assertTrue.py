# %%
from unittest import TestCase


def is_even(num):
    return num % 2 == 0


test_case = TestCase()
test_case.assertTrue(is_even(8))
