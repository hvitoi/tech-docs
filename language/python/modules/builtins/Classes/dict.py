# %%
# Access
my_dict = {"a": 1, "b": 2, "c": 3}

my_dict["b"]  # 2
# my_dict["z"]  # exception!

# %%
# Write
my_dict = {"a": 1, "b": 2, "c": 3}

my_dict["d"] = 4

my_dict

# %%
# Dict vs. Sets
its_a_dict = {}

its_a_dict["a"] = 1

its_a_dict

# empty sets can be initialized as {*()}


# %%
# Dict <-> Tuple convertion
my_dict = {"a": 1, "b": 2, "c": 3}
my_tuples = my_dict.items()
my_dict_back = dict(my_tuples)
my_dict_back

# %%
# dict from list of tuples
dict([("a", 1), ("b", 2)])

# %%
# dict from kwargs
dict(sape=4139, guido=4127, jack=4098)

# %%
# Duplicate keys are removed
dict.fromkeys("abcac")  # {'a': None, 'b': None, 'c': None}
list(dict.fromkeys("abcac"))  # a way to remove duplicate from a list
