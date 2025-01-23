# %%
# https://leetcode.com/problems/longest-common-subsequence/

import unittest


def longest_common_subsequence_dp(txt1: str, txt2: str) -> int:
    """
    A subsequence of a string is a new string generated from the original string with some characters (can be none)
    deleted without changing the relative order of the remaining characters.
    For example, "ace" is a subsequence of "abcde"

    "ab" (length 2) is the longest common subsequence of "axb" and "azb"
    """
    if txt1 == "" or txt2 == "":
        return 0

    # compare the first char of both strings
    if txt1[0] == txt2[0]:
        return 1 + longest_common_subsequence_dp(txt1[1:], txt2[1:])
    else:
        # backtrack! Explore 2 possible paths
        return max(
            longest_common_subsequence_dp(txt1[1:], txt2),  # remove a char from txt1
            longest_common_subsequence_dp(txt1, txt2[1:]),  # remove a char from txt2
        )


test_case = unittest.TestCase()

test_case.assertEqual(longest_common_subsequence_dp("abcde", "ace"), 3)
test_case.assertEqual(longest_common_subsequence_dp("abc", "abc"), 3)
test_case.assertEqual(longest_common_subsequence_dp("abc", "def"), 0)
test_case.assertEqual(longest_common_subsequence_dp("axb", "azb"), 2)
