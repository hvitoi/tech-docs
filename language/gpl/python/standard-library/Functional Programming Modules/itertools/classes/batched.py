# Creates batches in form of tuple of size n

# %%
import itertools

it = itertools.batched(["a", "b", "c", "d", "e"], 2)

list(it)
