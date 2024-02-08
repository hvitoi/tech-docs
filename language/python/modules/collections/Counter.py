# %%
# Returns a frequency map
# Works on any Iterable
import collections

c = collections.Counter(["a", "a", "z", "z", "z"])

c

# %%
# The most common frequencies
c.most_common(1)

# %%
# The original Iterable used to create the counter
list(c.elements())
