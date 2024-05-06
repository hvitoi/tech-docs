# %% ARRANGEMENT
from unittest import TestCase


type Combination = frozenset[int]


def gen_combinations(elements: set[int], k: int) -> set[Combination]:
    """
    n-choose-k problem
    """
    if k == 0:
        return {frozenset()}

    combinations = set()
    for el in elements:
        next_combinations = gen_combinations(elements - {el}, k - 1)
        combinations_starting_with_el = set(c.union({el}) for c in next_combinations)
        combinations.update(combinations_starting_with_el)

    return combinations


test_case = TestCase()

test_case.assertEqual(
    list(sorted(map(list, gen_combinations(set([1, 2, 3, 4]), 2)))),
    [
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
        [3, 4],
    ],
)
