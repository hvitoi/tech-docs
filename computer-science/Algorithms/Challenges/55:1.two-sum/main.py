# %%
from typing import List
from unittest import TestCase


# %%
# This variation returns a boolean whether at least one pair matches the target sum


def two_sum_brute_force(data: List[int], target_sum: int) -> bool:
    # O(n^2)
    n = len(data)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if data[i] + data[j] == target_sum:
                return True
    return False


def two_sum_from_both_sides(data: List[int], target_sum: int) -> bool:
    # This assumes that the list is sorted
    # O(n)
    low = 0
    high = len(data) - 1

    while low < high:
        current_sum = data[low] + data[high]
        if current_sum == target_sum:
            return True
        if current_sum < target_sum:
            low += 1
        if current_sum > target_sum:
            high -= 1
    return False


def two_sum_has_been_seen(data: List[int], target_sum: int) -> bool:
    # O(n)
    seen_numbers = set()
    for el in data:
        complement = target_sum - el
        if complement in seen_numbers:  # lookups on sets is O(1)
            return True
        seen_numbers.add(el)
    return False


test_case = TestCase()
for fn in {two_sum_brute_force, two_sum_from_both_sides, two_sum_has_been_seen}:
    test_case.assertEqual(fn([1, 2, 3, 9], 8), False)
    test_case.assertEqual(fn([1, 2, 4, 4], 8), True)
    test_case.assertEqual(fn([], 8), False)

# %%
# This variation returns the list of pairs that match the target sum


def two_sum_every_match(arr: list[int], target_sum: int):
    seenNumbers = set()
    pairs_with_matching_sum = set()

    for number in arr:
        complement = target_sum - number
        if complement in seenNumbers:
            pairs_with_matching_sum.add(tuple(sorted((number, complement))))
        seenNumbers.add(number)

    return pairs_with_matching_sum


test_case = TestCase()
test_case.assertEqual(two_sum_every_match([2, 6, 3, 9, 11], 9), {(3, 6)})
test_case.assertEqual(two_sum_every_match([2, 6, 3, 5, 9, 4], 9), {(3, 6), (4, 5)})
test_case.assertEqual(two_sum_every_match([4], 8), set())
test_case.assertEqual(two_sum_every_match([4, 4], 8), {(4, 4)})
test_case.assertEqual(two_sum_every_match([2, 6, 3, 3, 6, 9, 11], 9), {(3, 6)})

# %%
# This variation returns the indexes of the first pair that matches the target sum


def two_sum_return_index_brute_force(nums: List[int], target: int):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


test_case = TestCase()
test_case.assertEqual(two_sum_return_index_brute_force([2, 7, 11, 15], 9), [0, 1])
test_case.assertEqual(two_sum_return_index_brute_force([3, 2, 4], 6), [1, 2])
test_case.assertEqual(two_sum_return_index_brute_force([3, 3], 6), [0, 1])
