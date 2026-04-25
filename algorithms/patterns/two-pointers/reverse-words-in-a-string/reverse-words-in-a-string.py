# https://leetcode.com/problems/reverse-words-in-a-string/ - 10k likes (Apr/2026)
# %%


def reverse_words(s: str) -> str:
    return " ".join(reversed(s.split()))


def reverse_words2(s: str) -> str:
    return " ".join(s.split()[::-1])


for fn in {reverse_words, reverse_words2}:
    assert reverse_words("the sky is blue") == "blue is sky the"
    assert reverse_words("  hello world  ") == "world hello"
    assert reverse_words("a good   example") == "example good a"
