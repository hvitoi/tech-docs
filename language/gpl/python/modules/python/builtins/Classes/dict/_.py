# %%
my_dict = {"a": 1, "b": 2, "c": 3}

my_dict["b"]  # 2
# my_dict["z"]  # fails!

# %%
my_dict = {"a": 1, "b": 2, "c": 3}

my_dict["d"] = 4

my_dict


# %%
# from tuples
dict([("a", 1), ("b", 2)])

# %%
# from kwargs
dict(sape=4139, guido=4127, jack=4098)
