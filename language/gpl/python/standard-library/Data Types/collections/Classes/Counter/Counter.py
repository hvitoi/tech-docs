# %%
from collections import Counter, defaultdict
from functools import reduce

# Returns a frequency map
# Works on any Iterable

c = Counter(["a", "a", "z", "z", "z"])
dict(c)


# %%
# char_map from scratch
def frequency(col):
    freq = {}
    for el in col:
        freq[el] = freq.get(el, 0) + 1
    return freq


def frequency2(col):
    freq = {}
    for num in col:
        if num not in freq:
            freq[num] = 0
        freq[num] += 1
    return freq


def frequency3(col):
    freq = defaultdict(int)
    for num in col:
        freq[num] += 1
    return freq


sentence = "hey there! How are you?"
frequency(sentence)


# %%

sentence = "hey there! How are you?"

letter_e_occurrence = reduce(
    lambda acc, char: acc + 1 if char == "e" else acc, sentence, 0
)
letter_e_occurrence = sum(1 for char in sentence if char == "e")

letter_e_occurrence
