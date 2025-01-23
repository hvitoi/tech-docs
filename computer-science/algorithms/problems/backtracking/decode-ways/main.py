# %%
# https://leetcode.com/problems/decode-ways/

import unittest


def memoize_from_first_three_letters(fn):
    """
    the input 222222222222222 (15 digits) is reduced
    from 1973 calculations to 14 calculations with this memoization
    """
    cache = {}

    def look_or_miss(s):
        key = s[:3]
        if key not in cache:
            cache[key] = fn(s)
        return cache[key]

    return look_or_miss


@memoize_from_first_three_letters
def num_decodings(s: str) -> int:
    """
    O(2^n) without memoization
    O(n) with memoization
    """
    if len(s) >= 1 and int(s[0]) == 0:
        return 0

    if len(s) <= 1:
        return 1

    can_have_two_digits = (
        True
        if (len(s) >= 2) and (int(s[:2]) <= 26) and (len(s) == 2 or int(s[2]) != 0)
        else False
    )

    if can_have_two_digits:
        return num_decodings(s[1:]) + num_decodings(s[2:])
    else:
        return num_decodings(s[1:])


test_case = unittest.TestCase()
test_case.assertEqual(num_decodings("12"), 2)
test_case.assertEqual(num_decodings("226"), 3)
test_case.assertEqual(num_decodings("06"), 0)
test_case.assertEqual(num_decodings("2263"), 3)
