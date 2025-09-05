# %%
from collections import Counter
from unittest import TestCase


def length_of_longest_substring(s: str) -> int:
    for n in reversed(range(1, len(s) + 1)):
        for i in range(len(s) - n):
            subs = s[i : i + n]
            if all(el == 1 for el in Counter(subs).values()):
                return len(subs)
    return 0


def length_of_longest_substring2(s: str) -> int:
    n = len(s)
    while n > 0:
        for i in range(len(s) - n):
            subs = s[i : i + n]
            if all(el == 1 for el in Counter(subs).values()):
                return len(subs)
        n -= 1
    return 0


def length_of_longest_substring3(s: str) -> int:
    left = 0
    seen = {}
    output = 0

    for right, curr in enumerate(s):
        if curr in seen:
            left = max(left, seen[curr] + 1)
        output = max(output, right - left + 1)
        seen[curr] = right

    return output


def length_of_longest_substring_with_seen_chars(s: str) -> int:
    longest_size = 0
    seen_letters = set()

    for letter in s:
        if letter in seen_letters:
            seen_letters.clear()
        seen_letters.add(letter)
        longest_size = max(longest_size, len(seen_letters))

    return longest_size


test_case = TestCase()

for fn in {
    length_of_longest_substring,
    length_of_longest_substring2,
    length_of_longest_substring3,
    length_of_longest_substring_with_seen_chars,
}:
    test_case.assertEqual(fn("abcabcbb"), 3)
    test_case.assertEqual(fn("bbbbb"), 1)
    test_case.assertEqual(fn("pwwkew"), 3)
