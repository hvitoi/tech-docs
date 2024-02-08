# %%
import unittest


def unique_occurrences(arr: list) -> bool:
    occ_map = {}
    for el in arr:
        occ_map[el] = occ_map.get(el, 0) + 1
    occ = occ_map.values()
    return len(occ) == len(set(occ))


test_case = unittest.TestCase()

test_case.assertEqual(
    unique_occurrences([1, 2, 2, 1, 1, 3]),
    True,
)
test_case.assertEqual(
    unique_occurrences([1, 2]),
    False,
)
test_case.assertEqual(
    unique_occurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]),
    True,
)
