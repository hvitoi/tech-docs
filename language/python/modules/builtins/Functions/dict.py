# %%
my_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

my_dict["b"]  # 2
# my_dict["z"]  # exception!

# %%
my_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
my_tuples = my_dict.items()
my_dict_back = dict(my_tuples)
my_dict_back
