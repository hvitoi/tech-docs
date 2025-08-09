# %%
from collections import OrderedDict


my_dict = OrderedDict()
my_dict["a"] = 1
my_dict["b"] = 2
my_dict["c"] = 3

# make "a" as if it was the last to be inserted
my_dict.move_to_end("a")
