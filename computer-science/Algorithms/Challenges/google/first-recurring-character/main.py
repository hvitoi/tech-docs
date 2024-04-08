# %%
from typing import List
from unittest import TestCase


def first_recurring_character(arr: List[int]) -> int:
    seenCharacters = set()

    for character in arr:
        if character in seenCharacters:
            return character
        else:
            seenCharacters.add(character)

    return None


test_case = TestCase()

test_case.assertEqual(
    first_recurring_character([2, 5, 1, 2, 3, 5, 1, 2, 4]),
    2,
)

test_case.assertEqual(
    first_recurring_character([2, 1, 1, 2, 3, 5, 1, 2, 4]),
    1,
)

test_case.assertEqual(
    first_recurring_character([2, 3, 4, 5]),
    None,
)
