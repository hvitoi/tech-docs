# Just like a dict, but does not raise exception when an inexistent key is tried to be accessed
# %%
from collections import defaultdict

# A map that that has a default value (generated by the Callable function) on non-defined values

my_dict = defaultdict(lambda: 0)  # receives a Callable function
my_dict = defaultdict(int)  # same as above
# my_dict = defaultdict(int, {"a": 1}, 1)  # with initial value


# %%
# int factory
my_dict = defaultdict(int)

my_dict["a"] += 1
my_dict["a"]  # 1

my_dict["b"]  # 0

# %%
# list factory

my_dict = defaultdict(list)

my_dict["a"].append(1)