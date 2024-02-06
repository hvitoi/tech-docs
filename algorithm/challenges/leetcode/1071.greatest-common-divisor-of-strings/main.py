# %%
from unittest import TestCase


def gcd_of_strings(s1: str, s2: str) -> str:
    len_min = min(len(s1), len(s2))
    s = s1 + s2

    for i in range(len_min):
        print(i)
    # return s


test_case = TestCase()
test_case.assertEqual(gcd_of_strings("ABCABC", "ABC"), "ABC")
# test_case.assertEqual(gcd_of_strings("ABABAB", "ABAB"), "AB")
# test_case.assertEqual(gcd_of_strings("LEET", "CODE"), "")
