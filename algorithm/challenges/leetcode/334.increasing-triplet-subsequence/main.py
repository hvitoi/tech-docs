# %%
import unittest


def increasing_triplet(nums: list) -> bool:
    for i in range(len(nums) - 2):
        if nums[i] < nums[i + 1] < nums[i + 2]:
            return True
    return False


test_case = unittest.TestCase()
test_case.assertTrue(increasing_triplet([1, 2, 3, 4, 5]))
test_case.assertFalse(increasing_triplet([5, 4, 3, 2, 1]))
test_case.assertTrue(increasing_triplet([2, 1, 5, 0, 4, 6]))
