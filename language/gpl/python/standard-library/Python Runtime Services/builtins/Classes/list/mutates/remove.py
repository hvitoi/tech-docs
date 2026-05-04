# %%
my_list = ["a", "b", "c"]

my_list.remove("b")  # removes the FIRST element whose value is b

my_list

# %%
my_list.remove("z")  # ValueError: list.remove(x): x not in list
