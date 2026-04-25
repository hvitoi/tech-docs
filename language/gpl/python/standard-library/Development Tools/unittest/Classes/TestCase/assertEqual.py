# %%
from unittest import TestCase


def do_sum(a, b):
    return a + b


test_case = TestCase()
test_case.assertEqual(do_sum(1, 1), 2)
