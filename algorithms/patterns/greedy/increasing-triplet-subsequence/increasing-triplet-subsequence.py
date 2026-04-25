# https://leetcode.com/problems/increasing-triplet-subsequence/ - 8k likes (Apr/2026)
# %%


def increasing_triplet(nums: list) -> bool:
    for i in range(len(nums) - 2):
        if nums[i] < nums[i + 1] < nums[i + 2]:
            return True
    return False


assert increasing_triplet([1, 2, 3, 4, 5])
assert not increasing_triplet([5, 4, 3, 2, 1])
assert increasing_triplet([2, 1, 5, 0, 4, 6])
