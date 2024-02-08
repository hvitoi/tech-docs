# %%
import unittest
import itertools
import collections


def code_strings(word1: str, word2: str) -> bool:
    counter1 = collections.Counter(word1)
    counter2 = collections.Counter(word2)

    # Operation 1: any 2 chars can be swapped
    # -> Therefore the strings must have the same frequency map (be anagrams)

    # Operation 2: all the same letters can be swapped with another existing letter, the same will happen for the other letter
    # -> Therefore the frequency map for these 2 letters are simply swapped. Sorting it helps

    # return are_anagrams
    return sorted(counter1.values()) == sorted(counter2.values())


test_case = unittest.TestCase()


test_case.assertEqual(
    code_strings("abc", "bca"),
    True,
)
test_case.assertEqual(
    code_strings("a", "aa"),
    False,
)
test_case.assertEqual(
    code_strings("cabbba", "abbccc"),
    True,
)
