# %%
from unittest import TestCase


def frequency(coll):
    freq = {}
    for el in coll:
        freq[el] = freq.get(el, 0) + 1
    return freq


def min_window_brute_force(s: str, t: str) -> str:
    """Brute force solution"""

    def is_valid(subs):
        freq = frequency(subs)
        for c in t:
            if (c not in freq) or (freq[c] == 0):
                return False
            freq[c] -= 1
        return True

    for length in range(len(t), len(s) + 1):
        for i in range(len(s) - length + 1):
            subs = s[i : i + length]
            if is_valid(subs):
                return subs
    return ""


def min_window_two_pointers_and_frequency_map(s: str, t: str) -> str:
    """
    Move right to satisfy the solution (until the solution is satisfied)
    Move left to optimize the solution (until it breaks)
    """

    def is_valid(subs):
        freq = frequency(subs)
        for c in t:
            if (c not in freq) or (freq[c] == 0):
                return False
            freq[c] -= 1
        return True

    left = 0
    right = 0
    current_solution = ""

    while right < len(s) and left < len(s):
        subs = s[left : right + 1]
        if is_valid(subs):
            if not current_solution or len(subs) < len(current_solution):
                current_solution = subs
            left += 1
            continue
        right += 1
    return current_solution


test_case = TestCase()

for fn in {min_window_brute_force, min_window_two_pointers_and_frequency_map}:
    test_case.assertEqual(fn("ADOBECODEBANC", "ABC"), "BANC")
    test_case.assertEqual(fn("a", "a"), "a")
    test_case.assertEqual(fn("a", "aa"), "")
