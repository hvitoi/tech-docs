# %%
from typing import List
from unittest import TestCase


def two_sum(nums: List[int], target: int):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []  # no solution


test_case = TestCase()

test_case.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
test_case.assertEqual(two_sum([3, 2, 4], 6), [1, 2])
test_case.assertEqual(two_sum([3, 3], 6), [0, 1])
