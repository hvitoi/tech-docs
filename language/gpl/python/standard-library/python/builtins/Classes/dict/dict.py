# %%
# from list of tuples
dict([("a", 1), ("b", 2)])

# from kwargs
dict(a=1, b=2)

# %%
my_dict = {"a": 1, "b": 2}
my_dict["b"]  # 2 # access
# my_dict["z"]  # fails!
my_dict["c"] = 3  # write
my_dict

# %%
# Merge dicts (Python 3.9+)
{"a": 1} | {"b": 2}

# Dictionary update
d1 = {"a": 1}
d1 |= {"b": 2}  # same as dict1.update(...)
d1
