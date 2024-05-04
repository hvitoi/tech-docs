# Tuples are immutable

# %%
my_tuple = ("a", "b", "c")
my_tuple[0]  # "a"

# %%
my_tuple = ()  # empty tuple
my_tuple

# %%
# Concatenate tuples
(1, 2) + (3, 4)


# %%
def foo(*args, **kwargs):
    # args as tuple
    print(args)

    # kwargs as dict
    print(kwargs)


foo(1, 2, a=3, b=4)
