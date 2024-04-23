# %%
from unittest import TestCase


def partition(arr: list) -> int:
    """
    Rearrange the arr, moving:
       - the elements smaller than the pivot to the left
       - the elements greater than the pivot to the right

    The pivot is arbitrarily chosen as the first one in the arr
    """
    p = 0
    i = len(arr) - 1
    direction = "<-"

    while i != p:
        match direction:
            case "<-":
                if arr[i] < arr[p]:
                    arr[i], arr[p] = arr[p], arr[i]
                    i, p = p, i
                    direction = "->"
                else:
                    i -= 1
            case "->":
                if arr[i] > arr[p]:
                    arr[i], arr[p] = arr[p], arr[i]
                    i, p = p, i
                    direction = "<-"
                else:
                    i += 1
    return p


def partition2(arr):
    begin = 0
    pivot = begin

    for i in range(begin + 1, len(arr)):
        if arr[i] <= arr[begin]:
            pivot += 1
            arr[i], arr[pivot] = arr[pivot], arr[i]

    arr[pivot], arr[begin] = arr[begin], arr[pivot]
    return pivot


def quick_sort(arr: list):
    if len(arr) <= 1:
        return arr

    pivot_index = partition2(arr)
    left = arr[:pivot_index]
    right = arr[pivot_index + 1 :]

    return quick_sort(left) + [arr[pivot_index]] + quick_sort(right)


test_case = TestCase()
test_case.assertEqual(quick_sort([4, 5, 1, 3, 2]), [1, 2, 3, 4, 5])
test_case.assertEqual(quick_sort([]), [])
test_case.assertEqual(quick_sort([1]), [1])
test_case.assertEqual(quick_sort([1, 1]), [1, 1])
