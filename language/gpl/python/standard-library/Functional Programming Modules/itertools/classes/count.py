# %%
from itertools import count


it = count()
it = count(1)  # starts with 1

next(it)  # 1
next(it)  # 2
