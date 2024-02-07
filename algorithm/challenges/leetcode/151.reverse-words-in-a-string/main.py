# %%
from unittest import TestCase


def reverse_words(s: str) -> str:
    return " ".join(reversed(s.split()))


def reverse_words2(s: str) -> str:
    return " ".join(s.split()[::-1])


test_case = TestCase()

for fn in {reverse_words, reverse_words2}:
    test_case.assertEqual(reverse_words("the sky is blue"), "blue is sky the")
    test_case.assertEqual(reverse_words("  hello world  "), "world hello")
    test_case.assertEqual(reverse_words("a good   example"), "example good a")
