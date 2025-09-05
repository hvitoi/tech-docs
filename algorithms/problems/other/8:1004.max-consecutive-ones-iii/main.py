# %%
import unittest


def longest_ones(A: list, k: int) -> int:
    left = right = 0
    max_ones = 0
    while right < len(A):
        window = A[left : right + 1]
        max_ones = max(max_ones, window.count(1) + min(window.count(0), k))

        if window.count(0) <= k:
            right += 1
        else:
            left += 1

    return max_ones


test_case = unittest.TestCase()

test_case.assertEqual(longest_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), 6)
test_case.assertEqual(
    longest_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3), 10
)
test_case.assertEqual(
    longest_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3), 10
)

test_case.assertEqual(longest_ones([0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0], 2), 9)
test_case.assertEqual(longest_ones([1, 1, 1, 1, 1, 1], 2), 6)
