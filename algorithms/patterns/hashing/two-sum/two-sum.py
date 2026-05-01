# https://leetcode.com/problems/two-sum/ - 68k likes (Apr/2026)

# %%
import heapq


def two_sum_brute_force(nums: list[int], target_sum: int) -> bool:
    """
    O(n^2)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target_sum:
                return True
    return False


def two_sum_has_been_seen(nums: list[int], target_sum: int) -> bool:
    """
    O(n)
    """
    seen_numbers = set()
    for num in nums:
        complement = target_sum - num
        if complement in seen_numbers:
            return True
        seen_numbers.add(num)
    return False


def two_sum_from_both_sides(nums: list[int], target_sum: int) -> bool:
    """
    O(n)
    This assumes that the list is sorted
    """
    low = 0
    high = len(nums) - 1

    while low < high:
        current_sum = nums[low] + nums[high]
        if current_sum == target_sum:
            return True
        if current_sum < target_sum:
            low += 1
        if current_sum > target_sum:
            high -= 1
    return False


for fn in [two_sum_brute_force, two_sum_has_been_seen, two_sum_from_both_sides]:
    assert fn([1, 2, 3, 9], 8) is False
    assert fn([1, 2, 4, 4], 8) is True
    assert fn([], 8) is False


# %%
# This variation returns the list of pairs that match the target sum
def two_sum_every_match(nums: list[int], target_sum: int) -> set[tuple[int, int]]:
    pairs: set[tuple[int, int]] = set()
    seen_numbers: set[int] = set()

    for num in nums:
        complement = target_sum - num
        if complement in seen_numbers:
            pair = (min(num, complement), max(num, complement))  # sort the tuple
            pairs.add(pair)
        seen_numbers.add(num)

    return pairs


assert two_sum_every_match([2, 6, 3, 9, 11], 9) == {(3, 6)}
assert two_sum_every_match([2, 6, 3, 5, 9, 4], 9) == {(3, 6), (4, 5)}
assert two_sum_every_match([4], 8) == set()
assert two_sum_every_match([4, 4], 8) == {(4, 4)}
assert two_sum_every_match([2, 6, 3, 3, 6, 9, 11], 9) == {(3, 6)}
