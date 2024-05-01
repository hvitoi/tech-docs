# %%
{x: x**2 for x in (1, 2, 3, 4, 5)}

# %%
my_map = {"a": 0, "b": 1, "c": 2}
{k: my_map[k] for k in my_map if k != "b"}  # filter out the "b" key
