# %%
from collections import OrderedDict


my_dict = OrderedDict()
my_dict["a"] = 1
my_dict["b"] = 2
my_dict["c"] = 3

# pop the last item inserted
my_dict.popitem()  # 3

# pop the first item inserted
my_dict.popitem(last=False)  # 1
