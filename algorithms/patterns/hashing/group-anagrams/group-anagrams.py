# LeetCode #49 https://leetcode.com/problems/group-anagrams/ 22k likes (Apr-2026)
# %%


from collections import Counter


def add_string(groups, string, string_fm):
    for group, group_fm in groups:
        if string_fm == group_fm:
            group.append(string)
            group.sort()
            return
    groups.insert(0, ([string], string_fm))


def group_anagrams(strings: list[str]) -> list[list[str]]:
    fms = {}
    for string in strings:
        fms[string] = Counter(c.casefold() for c in string if c.isalpha())

    groups: list[tuple[list[str], Counter]] = []
    for string, string_fm in fms.items():
        add_string(groups, string, string_fm)

    return list(map(lambda el: el[0], groups))


assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
    ["bat"],
    ["nat", "tan"],
    ["ate", "eat", "tea"],
]

assert group_anagrams([""]) == [[""]]
assert group_anagrams(["a"]) == [["a"]]
