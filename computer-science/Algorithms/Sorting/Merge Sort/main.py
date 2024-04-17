# %%
from unittest import TestCase


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # sort each part
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # concatenate the two parts in the correct order
    if left[-1] <= right[0]:
        return left + right
    else:
        return right + left


test_case = TestCase()
test_case.assertEqual(merge_sort([4, 5, 1, 3, 2]), [1, 2, 3, 4, 5])
test_case.assertEqual(merge_sort([]), [])
test_case.assertEqual(merge_sort([2, 1, 1]), [1, 1, 2])
