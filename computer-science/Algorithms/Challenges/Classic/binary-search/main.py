# %%
from unittest import TestCase


def binary_search(arr, el):
    """O(log n)"""
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        if el == arr[mid]:
            return True

        if el < arr[mid]:
            high = mid - 1
            continue

        if el > arr[mid]:
            low = mid + 1
            continue

    return False


test_case = TestCase()

test_case.assertEqual(binary_search([1, 2, 3, 4, 5], 4), True)
test_case.assertEqual(binary_search([1, 2, 3, 4, 5], 99), False)
test_case.assertEqual(binary_search([], 99), False)
