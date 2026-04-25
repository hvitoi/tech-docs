# https://leetcode.com/problems/maximum-average-subarray-i/ - 4k likes (Apr/2026)
# %%


def find_max_average(nums: list, k: int) -> float:
    max_sum = float("-inf")
    for i in range(len(nums) - k + 1):
        subarray = nums[i : i + k]
        max_sum = max(max_sum, sum(subarray))
    return max_sum / k


assert find_max_average([1, 12, -5, -6, 50, 3], 4) == 12.75
assert find_max_average([5], 1) == 5.0
