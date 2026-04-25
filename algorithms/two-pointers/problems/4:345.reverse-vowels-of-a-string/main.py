# https://leetcode.com/problems/reverse-vowels-of-a-string/ - 5k likes (Apr/2026)
# %%


def reverse_vowels(s: str) -> str:
    s = list(s)

    vowels = {"a", "e", "i", "o", "u"}
    found_vowels = []

    for i, letter in enumerate(s):
        if letter.casefold() in vowels:
            found_vowels.append(letter)
            s[i] = None
    for i, letter in enumerate(s):
        if letter is None:
            s[i] = found_vowels.pop()

    return "".join(s)


assert reverse_vowels("hello") == "holle"
assert reverse_vowels("leetcode") == "leotcede"
