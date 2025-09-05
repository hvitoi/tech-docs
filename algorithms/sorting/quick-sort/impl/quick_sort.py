# %%
from unittest import TestCase


def partition2(arr: list[int]) -> int:
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


def quick_sort(arr: list[int]) -> list[int]:
    """
    """

    def partition(left: int, right: int) -> int:
        pivot_value = arr[right]  # pivot is the rightmost el (convention, could be any)
        pivot_index = left  # initial position of the pivot, elements to the left of this index (exclusive) should be lower than the pivot value
        for i in range(left, right):  # excludes the last element (the pivot)
            if arr[i] <= pivot_value:
                arr[pivot_index], arr[i] = arr[i], arr[pivot_index]
                pivot_index += 1
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]  # Bring pivot to the correct position
        return pivot_index  # return the pivot's final resting position

    def qs(left: int, right: int) -> None:
        if (right - left) <= 0:
            return

        pivot_index = partition(left, right)

        qs(left, pivot_index - 1)
        qs(pivot_index + 1, right)

    qs(0, len(arr) - 1)

    return arr


test_case = TestCase()
test_case.assertEqual(quick_sort([4, 5, 1, 3, 2]), [1, 2, 3, 4, 5])
test_case.assertEqual(quick_sort([]), [])
test_case.assertEqual(quick_sort([1]), [1])
test_case.assertEqual(quick_sort([1, 1]), [1, 1])
