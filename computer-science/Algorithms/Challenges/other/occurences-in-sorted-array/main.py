# %%
from unittest import TestCase


# We have a dictionary list. E.g [“apple”, “banana”, ...]
# Given a prefix, we want to return all the words from the above list which matches the prefix.


def occurrences_in_sorted_array(arr: list[str], prefix: str) -> int:
    """
    Find the left-most matching element (using binary search)
    Find the right-most matching element (using binary search)
    Slice the array with both indexes
    """

    def find_left_most_match(left, right):
        mid_index = left + (right - left) // 2
        mid_value = arr[mid_index]

        if prefix == mid_value[:prefix_len]:
            left_index = mid_index - 1
            left_value = arr[left_index] if left_index >= 0 else None
            if left_value and left_value[:prefix_len] == prefix:
                return find_left_most_match(left, mid_index - 1)
            return mid_index

        if prefix < mid_value[:prefix_len]:
            return find_left_most_match(left, mid_index - 1)

        if prefix > mid_value[:prefix_len]:
            return find_left_most_match(mid_index + 1, right)

    def find_right_most_match(left, right):
        mid_index = left + (right - left) // 2
        mid_value = arr[mid_index]

        if prefix == mid_value[:prefix_len]:
            right_index = mid_index + 1
            right_value = arr[right_index] if right_index < len(arr) else None
            if right_value and right_value[:prefix_len] == prefix:
                return find_right_most_match(mid_index + 1, right)
            return mid_index

        if prefix < mid_value[:prefix_len]:
            return find_right_most_match(left, mid_index - 1)

        if prefix > mid_value[:prefix_len]:
            return find_right_most_match(mid_index + 1, right)

    prefix_len = len(prefix)

    lower_bound = find_left_most_match(0, len(arr) - 1)
    upper_bound = find_right_most_match(0, len(arr) - 1)

    return upper_bound - lower_bound + 1


test_case = TestCase()

test_case.assertEqual(
    occurrences_in_sorted_array(["ab", "cca", "ccb", "cc", "ccd", "cce"], "cc"), 5
)
