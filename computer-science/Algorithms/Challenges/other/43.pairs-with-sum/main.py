# %%
from typing import List
from unittest import TestCase


def pairs_with_target_sum(arr: List[int], target_sum: int):
    seenNumbers = set()
    pairs_with_matching_sum = []

    for number in arr:
        complement = target_sum - number
        if complement in seenNumbers:
            pairs_with_matching_sum.append(sorted([number, complement]))
        seenNumbers.add(number)

    return pairs_with_matching_sum


test_case = TestCase()

test_case.assertEqual(
    pairs_with_target_sum([2, 6, 3, 9, 11], 9),
    [[3, 6]],
)

test_case.assertEqual(
    pairs_with_target_sum([2, 6, 3, 5, 9, 4], 9),
    [[3, 6], [4, 5]],
)

test_case.assertEqual(
    pairs_with_target_sum([2, 6, 3, 3, 6, 9, 11], 9),
    [[3, 6]],
)

test_case.assertEqual(
    pairs_with_target_sum([4], 8),
    [],
)

# test_case.assertEqual(
#     pairs_with_target_sum([4, 4], 8),
#     [[4, 4]],
# )
