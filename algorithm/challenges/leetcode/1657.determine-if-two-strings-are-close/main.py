# %%
import unittest
import itertools


def code_strings(word1: str, word2: str) -> bool:
    pass


test_case = unittest.TestCase()

test_case.assertTrue(code_strings("abc", "bca"))
test_case.assertFalse(code_strings("a", "aa"))
test_case.assertTrue(code_strings("cabbba", "abbccc"))
