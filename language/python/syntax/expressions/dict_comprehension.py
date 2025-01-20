# %%
{x: x**2 for x in (1, 2, 3, 4, 5)}

# %%
m = {"a": 0, "b": 1, "c": 2}
filtered_map = {k: m[k] for k in m if k != "b"}  # filter out the "b" key
filtered_map = dict(filter(lambda kv: kv[0] != "b", m.items()))
filtered_map
