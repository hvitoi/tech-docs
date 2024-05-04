# %%
from unittest import TestCase


def gen_permutations(coll: set[int], k: int):
    if len(coll) == 1:
        return [coll]

    permutations = []
    for el in coll:
        remaining_elements = coll - {el}
        permutations_for_el = [
            {el} + p for p in gen_permutations(remaining_elements, k - 1)
        ]
        permutations.extend(permutations_for_el)
    return permutations


test_case = TestCase()

test_case.assertEqual(gen_permutations(set([1, 2]), 2), None)
# test_case.assertEqual(gen_permutations(set([1, 2, 3]), 2), None)
