# %%
from unittest import TestCase


def binary_search(arr, target):
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


def binary_search_recursive(arr, target, *, left=None, right=None):
    """O(log n)"""
    if left is None:
        left = 0

    if right is None:
        right = len(arr) - 1

    if (right - left) < 0:
        return False

    mid_index = left + (right - left) // 2

    if target == arr[mid_index]:
        return True

    if target < arr[mid_index]:
        return binary_search_recursive(arr, target, left=left, right=mid_index - 1)

    if target > arr[mid_index]:
        return binary_search_recursive(arr, target, left=mid_index + 1, right=right)


test_case = TestCase()

for fn in {binary_search, binary_search_recursive}:
    test_case.assertEqual(fn([1, 2, 3, 4, 5], 4), True)
    test_case.assertEqual(fn([1, 2, 3, 4, 5], 99), False)
    test_case.assertEqual(fn([], 99), False)
