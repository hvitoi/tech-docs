# %%
from unittest import TestCase


def binary_search(arr: list[int], target: int) -> bool:
    """O(log n)"""
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        # mid = (right + left) // 2 # this is prone to overflow

        if target == arr[mid]:
            return True

        if target < arr[mid]:
            right = mid - 1
            continue

        if target > arr[mid]:
            left = mid + 1
            continue

    return False


def binary_search_recursive(arr: list[int], target: int):
    """O(log n)"""

    def binary_search(left: int, right: int):
        if (right - left) < 0:
            return False

        mid_index = left + (right - left) // 2

        if target == arr[mid_index]:
            return True

        if target < arr[mid_index]:
            return binary_search(left, mid_index - 1)

        if target > arr[mid_index]:
            return binary_search(mid_index + 1, right)

    return binary_search(0, len(arr) - 1)


test_case = TestCase()

for fn in {binary_search, binary_search_recursive}:
    test_case.assertEqual(fn([1, 2, 3, 4, 5], 4), True)
    test_case.assertEqual(fn([1, 2, 3, 4, 5], 99), False)
    test_case.assertEqual(fn([], 99), False)
