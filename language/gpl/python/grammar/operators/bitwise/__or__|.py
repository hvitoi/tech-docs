# %%
a = 6  # 0000 0110
b = 12  # 0000 1100

# bitwise "OR"
# both sides are always evaluated (no short-circuit)
a | b  # 0000 1110 (14)
a.__or__(b)

# %%
# dict merge
{"a": 1} | {"b": 2}
dict({"a": 1}).__or__({"b": 2})

# %%
# set merge
{1, 2} | {2, 3}
set({1, 2}).__or__({2, 3})
