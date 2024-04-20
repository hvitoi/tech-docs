# %%

from unittest import TestCase


def rotate_array(nums: list[int], k: int) -> None:
    """O(n)
    O(k): where k is the slice size (the complete array)
    """
    breakpoint = len(nums) - k
    return nums[breakpoint:] + nums[:breakpoint]


test_case = TestCase()
test_case.assertEqual(rotate_array([1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 1, 2, 3, 4])
test_case.assertEqual(rotate_array([-1, -100, 3, 99], 2), [3, 99, -1, -100])
test_case.assertEqual(rotate_array([1, 2, 3, 4, 5], 6), [5, 1, 2, 3, 4])
