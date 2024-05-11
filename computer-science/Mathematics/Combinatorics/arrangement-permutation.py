# %% ARRANGEMENT
from unittest import TestCase


def gen_arrangements(elements: set[int], k: int) -> list[list[int]]:
    """
    Arrangement
    """
    if k == 0:
        return [[]]

    arrangements = []
    for el in elements:
        next_arrangements = gen_arrangements(elements - {el}, k - 1)
        arrangements_starting_with_el = [[el] + p for p in next_arrangements]
        arrangements.extend(arrangements_starting_with_el)

    return arrangements


test_case = TestCase()

test_case.assertEqual(
    gen_arrangements(set(), 1),
    [],
)
test_case.assertEqual(
    gen_arrangements(set([1, 2, 3]), 0),
    [[]],
)
test_case.assertEqual(
    gen_arrangements(set([1, 2, 3]), 1),
    [[1], [2], [3]],
)
test_case.assertEqual(
    gen_arrangements(set([1, 2, 3]), 2),
    [
        [1, 2],
        [1, 3],
        [2, 1],
        [2, 3],
        [3, 1],
        [3, 2],
    ],
)

test_case.assertEqual(
    gen_arrangements(set([1, 2, 3]), 3),  # PERMUTATION (!!!)
    [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ],
)
