# Similar to get, but also sets a value

# %%
my_dict: dict = {"a": 1, "b": 2, "c": 3}

# Get the specified key, otherwise set it to None
my_dict.setdefault("a")

# Get the specified key, otherwise set a default value
my_dict.setdefault("z", 99)
