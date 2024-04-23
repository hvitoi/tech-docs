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
    # Here we make the right most element as pivot
    pivot = arr[-1]

    # We re-arrange the array such that
    # The elements smaller than the pivot are at left to the pivot
    # And the elements greater than the pivot are at right to the pivot
    i = -1  # elements to the left of this index (inclusive) are lower than the pivot
    for j in range(len(arr) - 1):  # excludes the last element (the pivot)
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # The pivot comes to its correct position
    # (i + 1) at this point still contains an item lower than the pivot
    arr[i + 1], arr[-1] = arr[-1], arr[i + 1]

    # Return the pivot's final resting position
    return i + 1


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
