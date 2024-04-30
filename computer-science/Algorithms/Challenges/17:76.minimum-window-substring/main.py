# %%
from unittest import TestCase


def includes(str1, str2):
    for char in str2:
        if char not in str:
            return False
    return True


def min_window(s: str, t: str) -> str:
    for length in range(1, len(s)):
        for i in range(len(s) - length):
            subs = s[i, i + length]
            if includes(subs, t):
                return subs


test_case = TestCase()
test_case.assertEqual(min_window("ADOBECODEBANC", "ABC"), "BANC")
