# %% [markdown]
# # Operations
#
# There are lots of operations with pandas that will be really useful to you, but don't fall into any distinct category. Let's show them here in this lecture:

# %%
import pandas as pd

df = pd.DataFrame(
    {
        "col1": [1, 2, 3, 4],
        "col2": [444, 555, 666, 444],
        "col3": ["abc", "def", "ghi", "xyz"],
    }
)
df.head()

# %%
df

# %% [markdown]
# ### Info on Unique Values

# %%
df["col2"].unique()  # Returns array of unique values

# %%
df["col2"].nunique()  # returns the number of unique values

# %%
df["col2"].value_counts()

# %% [markdown]
# ### Selecting Data

# %%
# Select from DataFrame using criteria from multiple columns
newdf = df[(df["col1"] > 2) & (df["col2"] == 444)]

# %%
newdf

# %% [markdown]
# ### Applying Functions


# %%
def times2(x):
    return x * 2


# %%
df["col1"].apply(times2)

# %%
df["col1"].apply(lambda x: x * 2)

# %%
df

# %%
df["col3"].apply(len)

# %%
df["col1"].sum()

# %%


# %% [markdown]
# ** Permanently Removing a Column**

# %%
df.drop("col1", axis=1)  # not inplace

# %%
df

# %%
del df["col1"]

# %%
df

# %% [markdown]
# ** Get column and index names: **

# %%
df.columns

# %%
df.index

# %% [markdown]
# ** Sorting and Ordering a DataFrame:**

# %%
df

# %%
df.sort_values(by="col2")  # inplace=False by default

# %% [markdown]
# ** Find Null Values or Check for Null Values**

# %%
df.isnull()

# %%
# Drop rows with NaN Values
df.dropna()

# %% [markdown]
# ** Filling in NaN values with something else: **

# %%
import numpy as np

# %%
df = pd.DataFrame(
    {
        "col1": [1, 2, 3, np.nan],
        "col2": [np.nan, 555, 666, 444],
        "col3": ["abc", "def", "ghi", "xyz"],
    }
)
df.head()

# %%
df.fillna("FILL")

# %%
data = {
    "A": ["foo", "foo", "foo", "bar", "bar", "bar"],
    "B": ["one", "one", "two", "two", "one", "one"],
    "C": ["x", "y", "x", "y", "x", "y"],
    "D": [1, 3, 2, 5, 4, 1],
}

df = pd.DataFrame(data)

# %%
df

# %%
df.pivot_table(values="D", index=["A", "B"], columns=["C"])
