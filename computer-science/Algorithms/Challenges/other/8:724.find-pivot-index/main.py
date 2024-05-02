# %%
import unittest


def pivot_index(nums: list) -> int:
    """
    O(n^2)
    n due to the iteration up to the target index
    n due to the sum of each part
    """
    for i in range(len(nums)):
        arr1 = nums[:i]
        arr2 = nums[i + 1 :]
        if sum(arr1) == sum(arr2):
            return i
    return -1


def pivot_index_with_two_sums_tracking(nums: list) -> int:
    """O(n)"""
    left_sum = 0
    right_sum = sum(nums)
    for i, num in enumerate(nums):
        right_sum -= num
        if left_sum == right_sum:
            return i
        left_sum += num
    return -1


test_case = unittest.TestCase()
for fn in {pivot_index, pivot_index_with_two_sums_tracking}:
    test_case.assertEqual(fn([1, 7, 3, 6, 5, 6]), 3)
    test_case.assertEqual(fn([1, 2, 3]), -1)
    test_case.assertEqual(fn([2, 1, -1]), 0)
