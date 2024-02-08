# Similar to my_dict[i], but allows more options and fallbacks
# %%
my_dict: dict = {"a": 1, "b": 2, "c": 3}

my_dict.get("a")

# %%
my_dict: dict = {"a": 1, "b": 2, "c": 3}
my_dict.get("z")  # returns None
my_dict.get("z", "foo")  # returns foo
