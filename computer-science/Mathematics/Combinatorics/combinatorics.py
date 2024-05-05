# %% ARRANGEMENT
from unittest import TestCase


def gen_arrangements(elements: set[int], k: int):
    if k == 0:
        return [[]]

    arrangements = []
    for el in elements:
        remaining_elements = elements - {el}
        arrangements_starting_with_el = [
            [el] + p for p in gen_arrangements(remaining_elements, k - 1)
        ]
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
    gen_arrangements(set([1, 2, 3]), 3),
    [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ],
)


# %% PERMUTATION
def gen_permutations_from_arrangement(elements: set[int]):
    return gen_arrangements(elements, len(elements))


def gen_permutations(elements: set[int]):
    if len(elements) == 0:
        return [[]]

    permutations = []
    for el in elements:
        remaining_elements = elements - {el}
        permutations_starting_with_el = [
            [el] + p for p in gen_permutations(remaining_elements)
        ]
        permutations.extend(permutations_starting_with_el)

    return permutations


test_case = TestCase()

for fn in {gen_permutations_from_arrangement, gen_permutations}:
    test_case.assertEqual(
        fn(set([1, 2, 3])),
        [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ],
    )


# %% COMBINATION
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
