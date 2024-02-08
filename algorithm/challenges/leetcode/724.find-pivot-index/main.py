# %%
import unittest


def pivot_index(nums: list) -> int:
    for i in range(len(nums)):
        arr1 = nums[:i]
        arr2 = nums[i + 1 :]
        if sum(arr1) == sum(arr2):
            return i
    return -1


test_case = unittest.TestCase()
test_case.assertEqual(pivot_index([1, 7, 3, 6, 5, 6]), 3)
test_case.assertEqual(pivot_index([1, 2, 3]), -1)
test_case.assertEqual(pivot_index([2, 1, -1]), 0)
