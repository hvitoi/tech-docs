# %%
from unittest import TestCase


def longest_palindrome(s: str) -> str:
    # Brute force
    # O(n^3)
    for length in range(len(s), 0, -1):  # n to 1
        for i in range(len(s) - length + 1):
            subs = s[i : i + length]
            if subs == "".join(reversed(subs)):
                return subs
    return ""


test_case = TestCase()

for fn in {longest_palindrome}:
    test_case.assertEqual(fn("babad"), "bab")
    test_case.assertEqual(fn("cbbd"), "bb")
