# %%
from unittest import TestCase


def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


test_case = TestCase()
test_case.assertEqual(selection_sort([4, 5, 1, 3, 2]), [1, 2, 3, 4, 5])
test_case.assertEqual(selection_sort([]), [])
test_case.assertEqual(selection_sort([1]), [1])
test_case.assertEqual(selection_sort([1, 1]), [1, 1])
