# %%
from unittest import TestCase


def gen_arrangements(nums: set[int], k: int):
    if k == 0:
        return [[]]

    arrangements = []
    for el in nums:
        remaining_elements = nums - {el}
        arrangements_for_el = [
            [el] + p for p in gen_arrangements(remaining_elements, k - 1)
        ]
        arrangements.extend(arrangements_for_el)

    return arrangements


def gen_permutations(coll: set[int]):
    return gen_arrangements(coll, len(coll))


test_case = TestCase()

test_case.assertEqual(gen_arrangements(set([1, 2, 3]), 0), [[]])
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
# test_case.assertEqual(gen_arrangements(set([1, 2, 3]), 3), None)
# test_case.assertEqual(gen_permutations(set([1, 2, 3]), 2), None)
