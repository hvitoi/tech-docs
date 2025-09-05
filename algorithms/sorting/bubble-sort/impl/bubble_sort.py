# %%
from unittest import TestCase


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


test_case = TestCase()
test_case.assertEqual(bubble_sort([4, 5, 1, 3, 2]), [1, 2, 3, 4, 5])
test_case.assertEqual(bubble_sort([]), [])
test_case.assertEqual(bubble_sort([1]), [1])
test_case.assertEqual(bubble_sort([1, 1]), [1, 1])
