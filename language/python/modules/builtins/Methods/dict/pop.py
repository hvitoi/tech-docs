# Mutates and returns the popped element
# %%
my_dict: dict = {"a": 1, "b": 2, "c": 3}

my_dict.pop("a")  # returns 1

my_dict

# %%
my_dict: dict = {"a": 1, "b": 2, "c": 3}

# my_dict.pop("z")  # Throws!
my_dict.pop("z", "nothing here")  # returns nothing here and the dict is unchanged
