# %%
from unittest import TestCase


def longest_palindrome(s: str) -> str:
    # Brute force
    # O(n^3)
    N = len(s)
    for n in reversed(range(1, N + 1)):
        for i in range(N - n + 1):
            subs = s[i : i + n]
            if subs == "".join(reversed(subs)):
                return subs
    return ""


test_case = TestCase()

for fn in {longest_palindrome}:
    test_case.assertEqual(fn("babad"), "bab")
    test_case.assertEqual(fn("cbbd"), "bb")
