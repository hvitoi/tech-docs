# %%
import itertools

# %%
it = itertools.repeat("abc", 3)
list(it)

# %%
it = itertools.repeat("abc", 3)
"".join(it)
