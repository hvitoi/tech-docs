# %%
import unittest


def number_of_vowels(s: str) -> int:
    vowels = {"a", "e", "i", "o", "u"}
    n = 0

    for letter in s:
        if letter in vowels:
            n += 1
    return n


def max_vowels(s: str, k: int) -> int:
    max_vowels = 0
    for i in range(len(s) - k + 1):
        max_vowels = max(max_vowels, number_of_vowels(s[i : i + k]))
    return max_vowels


test_case = unittest.TestCase()

test_case.assertEqual(max_vowels("abciiidef", 3), 3)
test_case.assertEqual(max_vowels("aeiou", 2), 2)
test_case.assertEqual(max_vowels("leetcode", 3), 2)
