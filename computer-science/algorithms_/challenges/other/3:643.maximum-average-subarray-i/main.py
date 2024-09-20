# %%
import unittest


def find_max_average(nums: list, k: int) -> float:
    max_sum = float("-inf")
    for i in range(len(nums) - k + 1):
        subarray = nums[i : i + k]
        max_sum = max(max_sum, sum(subarray))
    return max_sum / k


test_case = unittest.TestCase()

test_case.assertEqual(find_max_average([1, 12, -5, -6, 50, 3], 4), 12.75000)
test_case.assertEqual(find_max_average([5], 1), 5.00000)
