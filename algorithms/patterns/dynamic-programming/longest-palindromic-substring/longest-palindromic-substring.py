# https://leetcode.com/problems/longest-palindromic-substring/ - 32k likes (Apr/2026)
# %%


def longest_palindrome(s: str) -> str:
    # Brute force
    # O(n^3)
    for length in range(len(s), 0, -1):  # n to 1
        for i in range(len(s) - length + 1):
            subs = s[i : i + length]
            if subs == "".join(reversed(subs)):
                return subs
    return ""


for fn in {longest_palindrome}:
    assert fn("babad") == "bab"
    assert fn("cbbd") == "bb"
