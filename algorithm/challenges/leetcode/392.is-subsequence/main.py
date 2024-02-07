# %%
import unittest


def is_subsequence(s: str, t: str) -> bool:
    i = 0
    for letter in s:
        found_i = t.find(letter, i)
        if found_i != -1:
            i = found_i
        else:
            return False
    return True


def is_subsequence2(s: str, t: str) -> bool:
    if not s:
        return True

    found_i = t.find(s[0])
    if found_i == -1:
        return False
    else:
        return is_subsequence2(s[1:], t[found_i + 1 :])


test_case = unittest.TestCase()

for fn in {is_subsequence, is_subsequence2}:
    test_case.assertTrue(fn("abc", "ahbgdc"))
    test_case.assertFalse(fn("axc", "ahbgdc"))
