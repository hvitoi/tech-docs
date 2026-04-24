# %%
import unittest
import itertools


def longest_consecutive_ones(nums: list) -> int:
    longest = 0
    current = 0
    for num in nums:
        if num == 1:
            current += 1
        else:
            current = 0
        longest = max(longest, current)
    return longest


def longest_subarray(nums: list) -> int:
    longest = 0
    for i in range(len(nums)):
        longest = max(longest, longest_consecutive_ones(nums[:i] + nums[i + 1 :]))
    return longest


def longest_consecutive_ones2(nums: list) -> int:
    return max(
        itertools.accumulate(
            nums,
            lambda acc, el: acc + 1 if el == 1 else 0,
        )
    )


def longest_subarray2(nums: list) -> int:
    return max(
        [longest_consecutive_ones2(nums[:i] + nums[i + 1 :]) for i in range(len(nums))]
    )


test_case = unittest.TestCase()

for fn in {longest_subarray, longest_subarray2}:
    test_case.assertEqual(fn([1, 1, 0, 1]), 3)
    test_case.assertEqual(fn([0, 1, 1, 1, 0, 1, 1, 0, 1]), 5)
    test_case.assertEqual(fn([1, 1, 1]), 2)
