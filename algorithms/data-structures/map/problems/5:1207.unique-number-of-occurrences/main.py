# https://leetcode.com/problems/unique-number-of-occurrences/ - 5k likes (Apr/2026)
# %%


def unique_occurrences(arr: list) -> bool:
    occ_map = {}
    for el in arr:
        occ_map[el] = occ_map.get(el, 0) + 1
    occ = occ_map.values()
    return len(occ) == len(set(occ))


assert unique_occurrences([1, 2, 2, 1, 1, 3]) is True
assert unique_occurrences([1, 2]) is False
assert unique_occurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]) is True
