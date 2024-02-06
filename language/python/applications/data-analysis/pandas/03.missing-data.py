# %% [markdown]
# # Missing Data
#
# Let's show a few convenient methods to deal with Missing Data in pandas:

# %%
import numpy as np
import pandas as pd

# %%
df = pd.DataFrame({"A": [1, 2, np.nan], "B": [5, np.nan, np.nan], "C": [1, 2, 3]})

# %%
df

# %%
df.dropna()  # Drops rows with missing values

# %%
df.dropna(axis=1)  # Drops columns with missing values

# %%
df.dropna(thresh=2)  # Drops rows with less with 2 values

# %%
df.fillna(value="FILL VALUE")  # Fill NaN values

# %%
df["A"].fillna(value=df["A"].mean())  # Fill NaN from A with mean of the column
