# %%


from unittest import TestCase


def longest_increasing_subsequence(nums: list[int], prev=float("-inf")) -> int:
    """
    Choice: either pick of not the next element as part of the subsequence
    Constraint: the element has to be greater than the current
    Goal: maximize the subsequence length
    """

    if len(nums) == 0:
        return 0

    curr = nums[0]

    if curr > prev:
        return max(
            1 + longest_increasing_subsequence(nums[1:], curr),  # pick
            longest_increasing_subsequence(nums[1:], prev),  # not pick
        )

    else:
        return longest_increasing_subsequence(nums[1:], prev)  # not pick


test_case = TestCase()
test_case.assertEqual(longest_increasing_subsequence([]), 0)
test_case.assertEqual(longest_increasing_subsequence([1]), 1)
test_case.assertEqual(longest_increasing_subsequence([1, 2]), 2)
test_case.assertEqual(longest_increasing_subsequence([2, 1]), 1)
test_case.assertEqual(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]), 4)
test_case.assertEqual(longest_increasing_subsequence([0, 1, 0, 3, 2, 3]), 4)
test_case.assertEqual(longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7]), 1)
