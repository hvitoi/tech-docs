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


def gcd_of_strings2(s1: str, s2: str) -> str:
    s = s1 + s2

    substrings_lenghts = list(
        reversed([x for x in range(1, min(len(s1), len(s2)) + 1)])
    )
    substrings = list(map(lambda x: s[:x], substrings_lenghts))

    for subs in substrings:
        if s.count(subs) == len(s) / len(subs):
            return subs

    return ""


test_case = TestCase()

test_case.assertEqual(gcd_of_strings("ABCABC", "ABC"), "ABC")
test_case.assertEqual(gcd_of_strings("ABABAB", "ABAB"), "AB")
test_case.assertEqual(gcd_of_strings("LEET", "CODE"), "")

test_case.assertEqual(gcd_of_strings2("ABCABC", "ABC"), "ABC")
test_case.assertEqual(gcd_of_strings2("ABABAB", "ABAB"), "AB")
test_case.assertEqual(gcd_of_strings2("LEET", "CODE"), "")
