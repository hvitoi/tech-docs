# Just like a dict, but does not raise exception when an inexistent key is tried to be accessed
# %%
import collections


my_dict = collections.defaultdict(lambda: 0)  # receives a Callable function
my_dict = collections.defaultdict(int)  # same as above
my_dict = collections.defaultdict(int, {"a": 1}, 1)  # with initial value


# %%
# int factory
my_dict = collections.defaultdict(int)

my_dict["a"] += 1
my_dict["a"]  # 1

my_dict["b"]  # 0

# %%
# list factory

my_dict = collections.defaultdict(list)

my_dict["a"].append(1)
