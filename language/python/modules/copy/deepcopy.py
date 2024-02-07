# %%
import copy

l1 = ["a", "b", "c"]
l2 = copy.deepcopy(l1)

l1.append("d")
l2.append("z")

# two independent lists
l1
l2
