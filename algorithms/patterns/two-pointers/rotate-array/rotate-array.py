# https://leetcode.com/problems/rotate-array/ - 21k likes (Apr/2026)
# %%


def rotate_array(nums: list[int], k: int) -> list[int]:
    """
    O(n): due to slicing (the complete array)
    """
    breakpoint = len(nums) - k
    return nums[breakpoint:] + nums[:breakpoint]


assert rotate_array([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
assert rotate_array([-1, -100, 3, 99], 2) == [3, 99, -1, -100]
assert rotate_array([1, 2, 3, 4, 5], 6) == [5, 1, 2, 3, 4]
