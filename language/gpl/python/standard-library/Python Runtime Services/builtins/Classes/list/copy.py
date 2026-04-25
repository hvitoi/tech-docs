# %%
# Shallow copy
list1 = ["a", "b", "c"]
list2 = list1.copy()

assert list1 is not list2
