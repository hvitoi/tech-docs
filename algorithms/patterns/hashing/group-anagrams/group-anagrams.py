# LeetCode #49 https://leetcode.com/problems/group-anagrams/ 22k likes (Apr-2026)
# %%


from collections import Counter, defaultdict


def group_anagrams(strings: list[str]) -> list[list[str]]:
    """
    O(n k); where:
      - n is the number of strings (iteration)
      - k is the average length of a string (counting chars - frequency map)
    The key is a frozenset of [(char, count)] — hashable, order-independent.
    """

    groups: dict[frozenset[tuple[str, int]], list[str]] = defaultdict(list)
    for string in strings:
        fm = Counter(c.casefold() for c in string if c.isalpha())
        key = frozenset(fm.items())
        groups[key].append(string)

    return list(groups.values())


def test(actual, expected):
    assert {tuple(sorted(g)) for g in actual} == {tuple(sorted(g)) for g in expected}


test(
    group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
    [
        ["bat"],
        ["nat", "tan"],
        ["ate", "eat", "tea"],
    ],
)

test(group_anagrams([""]), [[""]])
test(group_anagrams(["a"]), [["a"]])
