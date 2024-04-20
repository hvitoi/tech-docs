# %%
import unittest


def find_difference(nums1: list, nums2: list) -> list:
    s1, s2 = set(nums1), set(nums2)

    return [
        list(s1.difference(s2)),
        list(s2.difference(s1)),
    ]


def find_difference2(nums1: list, nums2: list) -> list:
    return [
        [el for el in set(nums1) if el not in nums2],
        [el for el in set(nums2) if el not in nums1],
    ]


test_case = unittest.TestCase()

for fn in {find_difference, find_difference2}:
    test_case.assertEqual(
        fn([1, 2, 3], [2, 4, 6]),
        [[1, 3], [4, 6]],
    )

    test_case.assertEqual(
        fn([1, 2, 3, 3], [1, 1, 2, 2]),
        [[3], []],
    )
