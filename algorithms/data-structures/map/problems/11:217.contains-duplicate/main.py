# https://leetcode.com/problems/contains-duplicate/ - 13k likes (Apr/2026)
# %%


def contains_duplicate(nums: list[int]):
    seen_numbers = set()
    for el in nums:
        if el in seen_numbers:
            return True
        seen_numbers.add(el)
    return False


assert contains_duplicate([1, 2, 3, 1]) is True
assert contains_duplicate([1, 2, 3, 4]) is False
assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
