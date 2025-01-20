# %%
from unittest import TestCase


def insertion_sort(arr):
    for i in range(len(arr)):
        for j in range(i, 0, -1):  # go left (except the first item)
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]  # bubble sort (inverted)
            else:
                break  # means it's in the right place (no need to go over the other elements)
    return arr


test_case = TestCase()
test_case.assertEqual(insertion_sort([4, 5, 1, 3, 2]), [1, 2, 3, 4, 5])
test_case.assertEqual(insertion_sort([]), [])
test_case.assertEqual(insertion_sort([1]), [1])
test_case.assertEqual(insertion_sort([1, 1]), [1, 1])
