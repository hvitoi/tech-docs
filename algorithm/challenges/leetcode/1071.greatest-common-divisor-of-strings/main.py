# %%
from unittest import TestCase


def gcd_of_strings(s1: str, s2: str) -> str:
    subs_len_min = min(len(s1), len(s2))
    s = s1 + s2

    for subs_len in range(1, subs_len_min + 1).__reversed__():
        subs = s[:subs_len]
        if s.count(subs) == len(s) / subs_len:
            return subs

    return ""


test_case = TestCase()
test_case.assertEqual(gcd_of_strings("ABCABC", "ABC"), "ABC")
test_case.assertEqual(gcd_of_strings("ABABAB", "ABAB"), "AB")
test_case.assertEqual(gcd_of_strings("LEET", "CODE"), "")
