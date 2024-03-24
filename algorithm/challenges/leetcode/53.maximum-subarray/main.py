# %%
from itertools import accumulate
from typing import List
from unittest import TestCase


def max_sub_array(nums: List[int]) -> int:
    greatest_sum = 0
    for left in range(len(nums)):
        for right in range(left, len(nums)):
            greatest_sum = max(greatest_sum, sum(nums[left : right + 1]))
    return greatest_sum


def max_sub_array2(nums: List[int]) -> int:
    # Kadane's algorithm
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
    return max(nums)


def max_sub_array3(nums: List[int]) -> int:
    # Kadane's algorithm
    return max(
        accumulate(nums, lambda prev, curr: curr + prev if prev > 0 else curr),
    )


test_case = TestCase()

for fn in {max_sub_array, max_sub_array2, max_sub_array3}:
    test_case.assertEqual(fn([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
    test_case.assertEqual(fn([1]), 1)
    test_case.assertEqual(fn([5, 4, -1, 7, 8]), 23)
