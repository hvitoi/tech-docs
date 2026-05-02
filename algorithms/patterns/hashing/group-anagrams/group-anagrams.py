# LeetCode #49 https://leetcode.com/problems/group-anagrams/ 22k likes (Apr-2026)
# %%


from collections import defaultdict


def group_anagrams(strings: list[str]) -> list[list[str]]:
    """
    O(n k log k); where:
      - n is the number of strings (iteration)
      - k is the average length of a string (sorting)
    """

    groups: dict[str, list[str]] = defaultdict(list)
    for string in strings:
        key = tuple(sorted(c.casefold() for c in string if c.isalpha()))
        groups[key].append(string)
        groups[key].sort()

    return list(groups.values())


group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
# assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
#     ["bat"],
#     ["nat", "tan"],
#     ["ate", "eat", "tea"],
# ]

# assert group_anagrams([""]) == [[""]]
# assert group_anagrams(["a"]) == [["a"]]
