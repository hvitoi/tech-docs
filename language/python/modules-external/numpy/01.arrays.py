# %% [markdown]
# # NumPy
#
# NumPy (or Numpy) is a Linear Algebra Library for Python, the reason it is so important for Data Science with Python is that almost all of the libraries in the PyData Ecosystem rely on NumPy as one of their main building blocks.
#
# Numpy is also incredibly fast, as it has bindings to C libraries. For more info on why you would want to use Arrays instead of lists, check out this great [StackOverflow post](http://stackoverflow.com/questions/993984/why-numpy-instead-of-python-lists).
#
# We will only learn the basics of NumPy, to get started we need to install it!

# %% [markdown]
# ## Installation Instructions
#
# **It is highly recommended you install Python using the Anaconda distribution to make sure all underlying dependencies (such as Linear Algebra libraries) all sync up with the use of a conda install. If you have Anaconda, install NumPy by going to your terminal or command prompt and typing:**
#
#     conda install numpy
#
# **If you do not have Anaconda and can not install it, please refer to [Numpy's official documentation on various installation instructions.](http://docs.scipy.org/doc/numpy-1.10.1/user/install.html)**

# %% [markdown]
# ## Using NumPy
#
# Once you've installed NumPy you can import it as a library:

# %%
import numpy as np

# %% [markdown]
# Numpy has many built-in functions and capabilities. We won't cover them all but instead we will focus on some of the most important aspects of Numpy: vectors,arrays,matrices, and number generation. Let's start by discussing arrays.
#
# # Numpy Arrays
#
# NumPy arrays are the main way we will use Numpy throughout the course. Numpy arrays essentially come in two flavors: vectors and matrices. Vectors are strictly 1-d arrays and matrices are 2-d (but you should note a matrix can still have only one row or one column).
#
# Let's begin our introduction by exploring how to create NumPy arrays.
#
# ## Creating NumPy Arrays
#
# ### From a Python List
#
# We can create an array by directly converting a list or list of lists:

# %%
my_list = [1, 2, 3]
my_list

# %%
np.array(my_list)

# %%
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_matrix

# %%
np.array(my_matrix)

# %% [markdown]
# ## Built-in Methods
#
# There are lots of built-in ways to generate Arrays

# %% [markdown]
# ### arange
#
# Return evenly spaced values within a given interval.

# %%
np.arange(0, 10)

# %%
np.arange(0, 11, 2)

# %% [markdown]
# ### zeros and ones
#
# Generate arrays of zeros or ones

# %%
np.zeros(3)

# %%
np.zeros((5, 5))

# %%
np.ones(3)

# %%
np.ones((3, 3))

# %% [markdown]
# ### linspace
# Return evenly spaced numbers over a specified interval.

# %%
np.linspace(0, 10, 3)

# %%
np.linspace(0, 10, 50)

# %% [markdown]
# ## eye
#
# Creates an identity matrix

# %%
np.eye(4)

# %% [markdown]
# ## Random
#
# Numpy also has lots of ways to create random number arrays:
#
# ### rand
# Create an array of the given shape and populate it with
# random samples from a uniform distribution
# over ``[0, 1)``.

# %%
np.random.rand(2)

# %%
np.random.rand(5, 5)

# %% [markdown]
# ### randn
#
# Return a sample (or samples) from the "standard normal" distribution. Unlike rand which is uniform:

# %%
np.random.randn(2)

# %%
np.random.randn(5, 5)

# %% [markdown]
# ### randint
# Return random integers from `low` (inclusive) to `high` (exclusive).

# %%
np.random.randint(1, 100)

# %%
np.random.randint(1, 100, 10)

# %% [markdown]
# ## Array Attributes and Methods
#
# Let's discuss some useful attributes and methods or an array:

# %%
arr = np.arange(25)
ranarr = np.random.randint(0, 50, 10)

# %%
arr

# %%
ranarr

# %% [markdown]
# ## Reshape
# Returns an array containing the same data with a new shape.

# %%
arr.reshape(5, 5)

# %% [markdown]
# ### max,min,argmax,argmin
#
# These are useful methods for finding max or min values. Or to find their index locations using argmin or argmax

# %%
ranarr

# %%
ranarr.max()

# %%
ranarr.argmax()  # index of the maximum value

# %%
ranarr.min()

# %%
ranarr.argmin()  # index of the minimum value

# %% [markdown]
# ## Shape
#
# Shape is an attribute that arrays have (not a method):

# %%
# Vector
arr.shape  # attribute that shows the dimensions of the array

# %%
# Notice the two sets of brackets
arr.reshape(1, 25)

# %%
arr.reshape(1, 25).shape

# %%
arr.reshape(25, 1)

# %%
arr.reshape(25, 1).shape

# %% [markdown]
# ### dtype
#
# You can also grab the data type of the object in the array:

# %%
arr.dtype
