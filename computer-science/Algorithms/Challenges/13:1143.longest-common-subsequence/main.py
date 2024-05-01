# %%
# subsequences do not have to contiguous
from unittest import TestCase


def longest_common_subsequence_dp(txt1: str, txt2: str) -> int:
    """Solution with dynamic programming"""
    if len(txt1) == 0 or len(txt2) == 0:
        return 0

    txt1_current = txt1[0] if len(txt1) > 0 else ""
    txt2_current = txt2[0] if len(txt2) > 0 else ""

    if txt1_current != txt2_current:
        # backtracking! monitor 2 possible paths
        return max(
            longest_common_subsequence_dp(txt1[1:], txt2),
            longest_common_subsequence_dp(txt1, txt2[1:]),
        )
    else:
        return 1 + longest_common_subsequence_dp(txt1[1:], txt2[1:])


test_case = TestCase()

test_case.assertEqual(longest_common_subsequence_dp("abcde", "ace"), 3)
test_case.assertEqual(longest_common_subsequence_dp("abc", "abc"), 3)
test_case.assertEqual(longest_common_subsequence_dp("abc", "def"), 0)
