# %%
from unittest import TestCase


def find_kth_largest(nums: list[int], k: int) -> int:
    pass


test_case = TestCase()
test_case.assertEqual(find_kth_largest([3, 2, 1, 5, 6, 4], 2), 5)
test_case.assertEqual(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)
