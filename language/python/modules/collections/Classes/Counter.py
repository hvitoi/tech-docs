# %%
from collections import Counter

# Returns a frequency map
# Works on any Iterable

c = Counter(["a", "a", "z", "z", "z"])
dict(c)


# %%
# char_map from scratch
def frequency(coll):
    freq = {}
    for el in coll:
        freq[el] = freq.get(el, 0) + 1
    return freq


sentence = "hey there! How are you?"
frequency(sentence)


# %%
from functools import reduce

sentence = "hey there! How are you?"

letter_e_occurrence = reduce(
    lambda acc, char: acc + 1 if char == "e" else acc, sentence, 0
)
letter_e_occurrence = sum(1 for char in sentence if char == "e")

letter_e_occurrence
