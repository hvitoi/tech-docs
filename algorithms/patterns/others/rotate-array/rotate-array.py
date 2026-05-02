# https://leetcode.com/problems/rotate-array/ - 21k likes (Apr/2026)
# %%


def rotate_array(nums: list[int], k: int) -> list[int]:
    """
    O(n): due to slicing (the complete array)
    """
    n = len(nums)
    if n == 0:
        return []
    k %= n  # normalize for k>n

    pivot = len(nums) - k
    return nums[pivot:] + nums[:pivot]


assert rotate_array([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
assert rotate_array([-1, -100, 3, 99], 2) == [3, 99, -1, -100]
assert rotate_array([1, 2, 3, 4, 5], 6) == [5, 1, 2, 3, 4]
