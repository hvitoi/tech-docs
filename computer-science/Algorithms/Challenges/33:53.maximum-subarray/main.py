# %%
from itertools import accumulate
from unittest import TestCase


def maximum_subarray_windows_brute_force(nums: list[int]) -> int:
    """O(n^3)"""
    greatest_sum = 0
    for left in range(len(nums)):
        for right in range(left, len(nums)):
            greatest_sum = max(greatest_sum, sum(nums[left : right + 1]))
    return greatest_sum


def maximum_subarray_windows_brute_force_with_current_window_accumulator(
    nums: list[int],
) -> int:
    """O(n^2)"""
    greatest_sum = 0
    for left in range(len(nums)):
        current_window_sum = 0
        for right in range(left, len(nums)):
            current_window_sum += nums[right]
            greatest_sum = max(greatest_sum, current_window_sum)
    return greatest_sum


def maximum_subarray_kadane(nums: list[int]) -> int:
    """
    O(n)
    Subproblem question: what is the largest sum I can get from a subarray ending at index X
    At each index, do I want to start a new subarray or extend the previous subarray's highest sum
    """
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
    return max(nums)


def maximum_subarray_kadane_accumulator(nums: list[int]) -> int:
    # Kadane's algorithm
    return max(
        accumulate(nums, lambda prev, curr: curr + prev if prev > 0 else curr),
    )


test_case = TestCase()

for fn in {
    maximum_subarray_windows_brute_force,
    maximum_subarray_windows_brute_force_with_current_window_accumulator,
    maximum_subarray_kadane,
    maximum_subarray_kadane_accumulator,
}:
    test_case.assertEqual(fn([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
    test_case.assertEqual(fn([1]), 1)
    test_case.assertEqual(fn([5, 4, -1, 7, 8]), 23)
