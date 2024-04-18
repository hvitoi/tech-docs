# %%
from unittest import TestCase


def quick_sort(arr: list):
    if len(arr) <= 1:
        return arr

    pivot_index = 0
    i = len(arr) - 1
    direction = "<-"

    while i != pivot_index:
        match direction:
            case "<-":
                if arr[i] < arr[pivot_index]:
                    arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
                    i, pivot_index = pivot_index, i
                    direction = "->"
                else:
                    i -= 1
            case "->":
                if arr[i] > arr[pivot_index]:
                    arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
                    i, pivot_index = pivot_index, i
                    direction = "<-"
                else:
                    i += 1

    left = arr[:pivot_index]
    right = arr[pivot_index + 1 :]

    return quick_sort(left) + [arr[pivot_index]] + quick_sort(right)


test_case = TestCase()
test_case.assertEqual(quick_sort([4, 5, 1, 3, 2]), [1, 2, 3, 4, 5])
test_case.assertEqual(quick_sort([]), [])
test_case.assertEqual(quick_sort([1]), [1])
test_case.assertEqual(quick_sort([1, 1]), [1, 1])
