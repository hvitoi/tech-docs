# %%
from typing import List
from unittest import TestCase


def merge_sorted_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    if len(arr1) == 0:
        return arr2

    if len(arr2) == 0:
        return arr1

    i = j = 0
    merged = []
    while (i < len(arr1)) or (j < len(arr2)):
        el1 = arr1[i] if i < len(arr1) else None
        el2 = arr2[j] if j < len(arr2) else None

        if el1 is None:
            merged.append(el2)
            j += 1
            continue

        if el2 is None:
            merged.append(el1)
            i += 1
            continue

        if el1 < el2:
            merged.append(el1)
            i += 1
        else:
            merged.append(el2)
            j += 1
    return merged


test_case = TestCase()

test_case.assertEqual(
    merge_sorted_arrays([0, 3, 4, 31], [4, 6, 30]),
    [0, 3, 4, 4, 6, 30, 31],
)
test_case.assertEqual(
    merge_sorted_arrays([], [4, 6, 30]),
    [4, 6, 30],
)
