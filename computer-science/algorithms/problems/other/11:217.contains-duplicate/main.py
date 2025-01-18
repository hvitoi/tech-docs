# %%

from unittest import TestCase


def contains_duplicate(nums: list[int]):
    seen_numbers = set()
    for el in nums:
        if el in seen_numbers:
            return True
        seen_numbers.add(el)
    return False


test_case = TestCase()
test_case.assertEqual(contains_duplicate([1, 2, 3, 1]), True)
test_case.assertEqual(contains_duplicate([1, 2, 3, 4]), False)
test_case.assertEqual(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)
