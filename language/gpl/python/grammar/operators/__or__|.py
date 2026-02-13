# %%
7 | 3
int(7).__or__(3)  # bitwise "or"

# %%
# dict merge
{"a": 1} | {"b": 2}
dict({"a": 1}).__or__({"b": 2})

# %%
# set merge
{1, 2} | {2, 3}
set({1, 2}).__or__({2, 3})
