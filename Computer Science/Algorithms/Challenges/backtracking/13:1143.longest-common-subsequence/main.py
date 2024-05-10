# %%
# subsequences do not have to be contiguous
from unittest import TestCase


def longest_common_subsequence_dp(txt1: str, txt2: str) -> int:
    """Solution with dynamic programming"""
    if len(txt1) == 0 or len(txt2) == 0:
        return 0

    char1 = txt1[0] if len(txt1) > 0 else ""
    char2 = txt2[0] if len(txt2) > 0 else ""

    if char1 == char2:
        return 1 + longest_common_subsequence_dp(txt1[1:], txt2[1:])
    else:
        # backtrack! Explore 2 possible paths
        return max(
            longest_common_subsequence_dp(txt1[1:], txt2),  # remove a char from txt1
            longest_common_subsequence_dp(txt1, txt2[1:]),  # remove a char from txt2
        )


test_case = TestCase()

test_case.assertEqual(longest_common_subsequence_dp("abcde", "ace"), 3)
test_case.assertEqual(longest_common_subsequence_dp("abc", "abc"), 3)
test_case.assertEqual(longest_common_subsequence_dp("abc", "def"), 0)
