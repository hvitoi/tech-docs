# %%
from unittest import TestCase


def divide_by_zero(num):
    return num / 0


test_case = TestCase()

test_case.assertRaises(ZeroDivisionError, divide_by_zero, num=10)
test_case.assertRaises(ZeroDivisionError, divide_by_zero, 10)
