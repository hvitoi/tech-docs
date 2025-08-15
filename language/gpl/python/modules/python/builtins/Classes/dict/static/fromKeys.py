# %%
# Duplicate keys are removed
my_dict = dict.fromkeys("abcac")  # {'a': None, 'b': None, 'c': None}

list(my_dict)

# %%
# Initialize with a default value
dict.fromkeys(["a", "b", "c"], 0)
