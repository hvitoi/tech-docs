# Tuples are immutable

# %%
my_tuple: tuple[str, ...] = ("a", "b", "c")
my_tuple[0]  # "a"

# %%
tp = ()  # empty tuple
tp = (1,)  # one element tuple
tp = (1, 2)  # two elements tuple
tp

# %%
# Concatenate tuples
(1, 2) + (3, 4)
