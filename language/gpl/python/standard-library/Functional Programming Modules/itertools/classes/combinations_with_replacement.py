# %%
import itertools

# same as "combinations" but allows repeated elements
it = itertools.combinations_with_replacement("ABC", 2)

list(it)
