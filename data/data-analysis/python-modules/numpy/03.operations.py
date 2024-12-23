# %% [markdown]
# # NumPy Operations

# %% [markdown]
# ## Arithmetic
#
# You can easily perform array with array arithmetic, or scalar with array arithmetic. Let's see some examples:

# %%
import numpy as np

arr = np.arange(0, 10)

# %%
arr + arr

# %%
arr * arr

# %%
arr - arr

# %%
# Warning on division by zero, but not an error!
# Just replaced with nan
arr / arr

# %%
# Also warning, but not an error instead infinity
1 / arr

# %%
arr**3

# %% [markdown]
# ## Universal Array Functions
#
# Numpy comes with many [universal array functions](http://docs.scipy.org/doc/numpy/reference/ufuncs.html), which are essentially just mathematical operations you can use to perform the operation across the array. Let's show some common ones:

# %%
# Taking Square Roots
np.sqrt(arr)

# %%
# Calcualting exponential (e^)
np.exp(arr)

# %%
np.max(arr)  # same as arr.max()

# %%
np.sin(arr)

# %%
np.log(arr)
