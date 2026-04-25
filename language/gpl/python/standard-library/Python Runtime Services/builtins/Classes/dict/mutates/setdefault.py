# %%
# It's a simple "get" if the element exists

my_dict = {"a": 1, "b": 2, "c": 3}
my_dict.setdefault("a")  # returns 1
my_dict.setdefault("z")  # returns None
my_dict

# %%
# If the element does not exist, set a value for it
my_dict: dict = {"a": 1, "b": 2, "c": 3}

my_dict.setdefault("y")  # set it to "None" and return "None"
my_dict.setdefault("z", 99)  # set it to "99" and return "99"
my_dict
