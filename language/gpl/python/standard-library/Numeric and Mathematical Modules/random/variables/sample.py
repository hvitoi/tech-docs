# %%
import random

# get k unique elements (without replacement)
# k must be <= len(population)

random.sample(range(100), k=5)
random.sample(["a", "b", "c"], k=2)
