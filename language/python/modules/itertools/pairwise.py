# %%
import itertools

# Creates an Iterable with each consecutive elements
# Final result is size n-1
it = itertools.pairwise([1, 2, 3, 4])

list(it)
