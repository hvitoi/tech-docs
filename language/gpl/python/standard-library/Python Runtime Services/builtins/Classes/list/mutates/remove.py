# %%
my_list = ["a", "b", "c"]

my_list.remove("b")  # removes the FIRST element whose value is b

my_list

# %%
my_list.remove("z")  # ValueError: list.remove(x): x not in list

# %%
# Remo all - inefficient O(n^2)
my_list = ["a", "b", "a", "c", "a"]

while True:
    try:
        my_list.remove("a")
    except ValueError:
        break

my_list

# %%
my_list = ["a", "b", "a", "c", "a"]

my_list[:] = [el for el in my_list if el != "a"]  # mutate existing list
my_list = [el for el in my_list if el != "a"]  # rebinds to a new list
