# https://leetcode.com/problems/merge-strings-alternately/ - 4k likes (Apr/2026)
# %%
from itertools import zip_longest


def merge_alternately(word1: str, word2: str) -> str:
    """
    Merge two strings
    """
    word1 = list(word1)
    word2 = list(word2)
    merged = []

    while len(word1) + len(word2) > 0:
        if len(word1) > 0:
            merged.append(word1.pop(0))
        if len(word2) > 0:
            merged.append(word2.pop(0))

    return "".join(merged)


def merge_alternately2(w1, w2):
    return "".join(a + b for a, b in zip_longest(w1, w2, fillvalue=""))


for fn in [merge_alternately, merge_alternately2]:
    assert fn("abc", "123") == "a1b2c3"
    assert fn("abc", "123") == "a1b2c3"
