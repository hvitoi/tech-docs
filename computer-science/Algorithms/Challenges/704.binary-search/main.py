# %%
from unittest import TestCase


def binary_search(arr, target):
    """O(log n)"""
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        if target == arr[mid]:
            return True

        if target < arr[mid]:
            high = mid - 1
            continue

        if target > arr[mid]:
            low = mid + 1
            continue

    return False


def binary_search_recursive(arr, target):
    """O(log n)"""
    if not arr:
        return False

    mid_index = len(arr) // 2

    if target == arr[mid_index]:
        return True

    if target < arr[mid_index]:
        return binary_search_recursive(arr[:mid_index], target)

    if target > arr[mid_index]:
        return binary_search_recursive(arr[mid_index + 1 :], target)


test_case = TestCase()

for fn in {binary_search, binary_search_recursive}:
    test_case.assertEqual(fn([1, 2, 3, 4, 5], 4), True)
    test_case.assertEqual(fn([1, 2, 3, 4, 5], 99), False)
    test_case.assertEqual(fn([], 99), False)
