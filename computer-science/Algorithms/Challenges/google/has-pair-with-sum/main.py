# %%
from typing import List
from unittest import TestCase


def hasPairWithSumBruteForce(data: List[int], target_sum: int) -> bool:
    # O(n^2)
    n = len(data)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if data[i] + data[j] == target_sum:
                return True
    return False


def hasPairWithSumFromBothSides(data: List[int], target_sum: int) -> bool:
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


def hasPairWithSumHasBeenSeen(data: List[int], target_sum: int) -> bool:
    # O(n)
    seen_numbers = set()
    for el in data:
        complement = target_sum - el
        if complement in seen_numbers:  # lookups on sets is O(1)
            return True
        seen_numbers.add(el)
    return False


test_case = TestCase()

for fn in {
    hasPairWithSumBruteForce,
    hasPairWithSumFromBothSides,
    hasPairWithSumHasBeenSeen,
}:
    test_case.assertEqual(fn([1, 2, 3, 9], 8), False)
    test_case.assertEqual(fn([1, 2, 4, 4], 8), True)
    test_case.assertEqual(fn([], 8), False)


# %%
# This variation returns the list of pairs that match the target sum
# Instead of returning if at least one pair matches the target sum


def pairs_with_target_sum(arr: list[int], target_sum: int):
    seenNumbers = set()
    pairs_with_matching_sum = set()

    for number in arr:
        complement = target_sum - number
        if complement in seenNumbers:
            pairs_with_matching_sum.add(tuple(sorted((number, complement))))
        seenNumbers.add(number)

    return pairs_with_matching_sum


test_case = TestCase()

test_case.assertEqual(pairs_with_target_sum([2, 6, 3, 9, 11], 9), {(3, 6)})
test_case.assertEqual(pairs_with_target_sum([2, 6, 3, 5, 9, 4], 9), {(3, 6), (4, 5)})
test_case.assertEqual(pairs_with_target_sum([4], 8), set())
test_case.assertEqual(pairs_with_target_sum([4, 4], 8), {(4, 4)})
test_case.assertEqual(pairs_with_target_sum([2, 6, 3, 3, 6, 9, 11], 9), {(3, 6)})
