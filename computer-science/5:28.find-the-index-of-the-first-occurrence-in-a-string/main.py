# %%
from unittest import TestCase


def find_str_brute_force(word: str, prefix: str) -> int:
    def matches(start):
        for i, prefix_letter in enumerate(prefix):
            if prefix_letter != word[start + i]:
                return False
        return True

    for i, letter in enumerate(word):
        if letter == prefix[0]:
            if matches(i):
                return i

    return -1


test_case = TestCase()
test_case.assertEqual(find_str_brute_force("sadbutsad", "sad"), 0)
test_case.assertEqual(find_str_brute_force("leetcode", "leeto"), -1)
test_case.assertEqual(find_str_brute_force("Henrique", "riq"), 3)
