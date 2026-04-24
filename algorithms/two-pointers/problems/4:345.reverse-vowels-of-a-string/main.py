# %%
from unittest import TestCase


def reverse_vowels(s: str) -> str:
    s = list(s)

    vowels = {"a", "e", "i", "o", "u"}
    found_vowels = []

    for i, letter in enumerate(s):
        if letter.casefold() in vowels:
            found_vowels.append(letter)
            s[i] = None
    for i, letter in enumerate(s):
        if letter is None:
            s[i] = found_vowels.pop()

    return "".join(s)


test_case = TestCase()

test_case.assertEqual(reverse_vowels("hello"), "holle")
test_case.assertEqual(reverse_vowels("leetcode"), "leotcede")
