# https://leetcode.com/problems/reverse-string/ - 9k likes (Apr/2026)
# %%


def reverse_string(original_string: str) -> str:
    reversed_string = ""
    for i in reversed(range(len(original_string))):
        reversed_string += original_string[i]
    return reversed_string


assert reverse_string("Hi, I'm Henrique") == "euqirneH m'I ,iH"
assert reverse_string("hello") == "olleh"
assert reverse_string("Hannah") == "hannaH"
