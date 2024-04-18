# %%
from unittest import TestCase


def quick_sort(arr: list):
    if len(arr) <= 1:
        return arr

    pivot_index = len(arr) // 2

    left = []
    right = []

    for i in range(len(arr)):
        if i == pivot_index:
            continue

        if arr[i] <= arr[pivot_index]:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [arr[pivot_index]] + quick_sort(right)


test_case = TestCase()
test_case.assertEqual(quick_sort([4, 5, 1, 3, 2]), [1, 2, 3, 4, 5])
test_case.assertEqual(quick_sort([]), [])
test_case.assertEqual(quick_sort([1]), [1])
test_case.assertEqual(quick_sort([1, 1]), [1, 1])
