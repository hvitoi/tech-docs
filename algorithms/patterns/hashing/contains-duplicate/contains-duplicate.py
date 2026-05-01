# https://leetcode.com/problems/contains-duplicate/ - 13k likes (Apr/2026)

# %%
def contains_duplicate(nums: list[int]) -> bool:
    seen_numbers = set()
    for num in nums:
        if num in seen_numbers:
            return True
        seen_numbers.add(num)
    return False


assert contains_duplicate([1, 2, 3, 1]) is True
assert contains_duplicate([1, 2, 3, 4]) is False
assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
