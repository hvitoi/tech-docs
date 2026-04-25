# %%
from copy import deepcopy

l1 = ["a", "b", "c"]
l2 = deepcopy(l1)

l1.append("d")
l2.append("z")

# two independent lists
l1
l2
