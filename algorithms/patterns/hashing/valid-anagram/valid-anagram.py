# %%
from collections import Counter, defaultdict


def charmap(string: str) -> dict[str, int]:
    frequency_map = defaultdict(int)
    for c in string:
        if c.isalpha():
            frequency_map[c.casefold()] += 1
    return frequency_map


def charmap2(string: str) -> dict[str, int]:
    frequency_map = Counter(c.casefold() for c in string if c.isalpha())
    return frequency_map


def valid_anagram(s1: str, s2: str) -> bool:
    return charmap(s1) == charmap(s2)


def valid_anagram2(s1: str, s2: str) -> bool:
    return charmap2(s1) == charmap2(s2)


for fn in [valid_anagram, valid_anagram2]:
    assert fn("rail safety", "fairy tales") is True
    assert fn("RAIL! SAFETY!", "fairy tales") is True
    assert fn("Hi there", "Bye there") is False
