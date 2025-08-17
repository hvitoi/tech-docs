# %%
import itertools

list1 = [1, 2, 3]
list2 = [4, 5, 6]

it = itertools.chain(list1, list2)
list(it)
