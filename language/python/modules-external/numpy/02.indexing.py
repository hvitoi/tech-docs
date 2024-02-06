# %% [markdown]
# # NumPy Indexing and Selection
#
# In this lecture we will discuss how to select elements or groups of elements from an array.

# %%
import numpy as np

# %%
# Creating sample array
arr = np.arange(0, 11)

# %%
# Show
arr

# %% [markdown]
# ## Bracket Indexing and Selection
# The simplest way to pick one or some elements of an array looks very similar to python lists:

# %%
# Get a value at an index
arr[8]

# %%
# Get values in a range
arr[1:5]

# %%
# Get values in a range
arr[0:5]

# %% [markdown]
# ## Broadcasting
#
# Numpy arrays differ from a normal Python list because of their ability to broadcast:

# %%
# Setting a value with index range (Broadcasting)
arr[0:5] = 100

# Show
arr

# %%
# Reset array, we'll see why I had to reset in  a moment
arr = np.arange(0, 11)

# Show
arr

# %%
# Important notes on Slices
slice_of_arr = arr[
    0:6
]  # slice_of_arr references to the same espace in memory of the arr array!!!

# Show slice
slice_of_arr

# %%
# Change Slice
slice_of_arr[:] = 99

# Show Slice again
slice_of_arr

# %% [markdown]
# Now note the changes also occur in our original array!

# %%
arr

# %% [markdown]
# Data is not copied, it's a view of the original array! This avoids memory problems!

# %%
# To get a copy, need to be explicit
arr_copy = arr.copy()

arr_copy

# %% [markdown]
# ## Indexing a 2D array (matrices)
#
# The general format is **arr_2d[row][col]** or **arr_2d[row,col]**. I recommend usually using the comma notation for clarity.

# %%
arr_2d = np.array(([5, 10, 15], [20, 25, 30], [35, 40, 45]))

# Show
arr_2d

# %%
# Indexing row
arr_2d[1]


# %%
# Format is arr_2d[row][col] or arr_2d[row,col]

# Getting individual element value
arr_2d[1][0]

# %%
# Getting individual element value
arr_2d[1, 0]

# %%
# 2D array slicing

# Shape (2,2) from top right corner
arr_2d[:2, 1:]

# %%
# Shape bottom row
arr_2d[2]

# %%
# Shape bottom row
arr_2d[2, :]

# %%
arr_2d[2]

# %% [markdown]
# ### Fancy Indexing
#
# Fancy indexing allows you to select entire rows or columns out of order,to show this, let's quickly build out a numpy array:

# %%
# Set up matrix
arr2d = np.zeros((10, 10))

# %%
# Length of array
arr_length = arr2d.shape[1]

# %%
arr_length

# %%
# Set up array

for i in range(arr_length):
    arr2d[i] = i

arr2d

# %% [markdown]
# Fancy indexing allows the following

# %%
arr2d[[2, 4, 6, 8]]

# %%
# Allows in any order
arr2d[[6, 4, 2, 7]]

# %% [markdown]
# ## More Indexing Help
# Indexing a 2d matrix can be a bit confusing at first, especially when you start to add in step size. Try google image searching NumPy indexing to fins useful images, like this one:
#
# <img src= 'http://memory.osu.edu/classes/python/_images/numpy_indexing.png' width=500/>

# %% [markdown]
# ## Selection
#
# Let's briefly go over how to use brackets for selection based off of comparison operators.

# %%
arr = np.arange(1, 11)
arr

# %%
arr > 4

# %%
bool_arr = arr > 4

# %%
bool_arr

# %%
arr[bool_arr]  # Returns only the values with True in the bool_arr

# %%
arr[arr > 2]

# %%
x = 2
arr[arr > x]
