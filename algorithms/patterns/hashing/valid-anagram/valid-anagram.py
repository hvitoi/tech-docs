# %%
from collections import Counter, defaultdict


def valid_anagram(s1: str, s2: str) -> bool:
    def charmap(string: str) -> dict[str, int]:
        frequency_map = defaultdict(int)
        for c in string:
            if c.isalpha():
                frequency_map[c.casefold()] += 1
        return frequency_map

    return charmap(s1) == charmap(s2)


def valid_anagram2(s1: str, s2: str) -> bool:
    def charmap(string: str) -> dict[str, int]:
        frequency_map = Counter(c.casefold() for c in string if c.isalpha())
        return frequency_map

    return charmap(s1) == charmap(s2)


def valid_anagram3(s1: str, s2: str) -> bool:
    """
    O(n log n); where n = s1 + s2
    """
    s1_sorted = str(sorted(c.casefold() for c in s1 if c.isalpha()))
    s2_sorted = str(sorted(c.casefold() for c in s2 if c.isalpha()))
    return s1_sorted == s2_sorted


for fn in [valid_anagram, valid_anagram2, valid_anagram3]:
    assert fn("rail safety", "fairy tales") is True
    assert fn("RAIL! SAFETY!", "fairy tales") is True
    assert fn("Hi there", "Bye there") is False
