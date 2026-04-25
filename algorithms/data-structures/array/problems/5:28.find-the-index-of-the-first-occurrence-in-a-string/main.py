# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/ - 7k likes (Apr/2026)
# %%


def find_str_brute_force(word: str, prefix: str) -> int:
    def matches(start):
        for i, prefix_letter in enumerate(prefix):
            if prefix_letter != word[start + i]:
                return False
        return True

    for i, letter in enumerate(word):
        if letter == prefix[0]:
            if matches(i):
                return i

    return -1


assert find_str_brute_force("sadbutsad", "sad") == 0
assert find_str_brute_force("leetcode", "leeto") == -1
assert find_str_brute_force("Henrique", "riq") == 3
