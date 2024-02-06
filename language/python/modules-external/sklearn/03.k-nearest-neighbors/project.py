# %% [markdown]
# # K Nearest Neighbors Project
#
# Welcome to the KNN Project! This will be a simple project very similar to the lecture, except you'll be given another data set. Go ahead and just follow the directions below.
# ## Import Libraries
# **Import pandas,seaborn, and the usual libraries.**

# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# %% [markdown]
# ## Get the Data
# ** Read the 'KNN_Project_Data csv file into a dataframe **

# %%
df = pd.read_csv("KNN_Project_Data")

# %% [markdown]
# **Check the head of the dataframe.**

# %%
df.head()

# %% [markdown]
# # EDA
#
# Since this data is artificial, we'll just do a large pairplot with seaborn.
#
# **Use seaborn on the dataframe to create a pairplot with the hue indicated by the TARGET CLASS column.**

# %%
sns.pairplot(data=df)

# %%
sns.pairplot(data=df, hue="TARGET CLASS", diag_kind="hist")

# %% [markdown]
# # Standardize the Variables
#
# Time to standardize the variables.
#
# ** Import StandardScaler from Scikit learn.**

# %%
from sklearn.preprocessing import StandardScaler

# %% [markdown]
# ** Create a StandardScaler() object called scaler.**

# %%
scaler = StandardScaler()

# %% [markdown]
# ** Fit scaler to the features.**

# %%
scaler.fit(df.drop("TARGET CLASS", axis=1))

# %% [markdown]
# **Use the .transform() method to transform the features to a scaled version.**

# %%
scaled_features = scaler.transform(df.drop("TARGET CLASS", axis=1))

# %%


# %% [markdown]
# **Convert the scaled features to a dataframe and check the head of this dataframe to make sure the scaling worked.**

# %%
df.columns[:2]

# %%
X = pd.DataFrame(scaled_features, columns=df.columns[:-1])
X.head()

# %%
y = df["TARGET CLASS"]
y

# %% [markdown]
# # Train Test Split
#
# **Use train_test_split to split your data into a training set and a testing set.**

# %%
from sklearn.model_selection import train_test_split

# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

# %% [markdown]
# # Using KNN
#
# **Import KNeighborsClassifier from scikit learn.**

# %%
from sklearn.neighbors import KNeighborsClassifier

# %% [markdown]
# **Create a KNN model instance with n_neighbors=1**

# %%
knn = KNeighborsClassifier(n_neighbors=1)

# %% [markdown]
# **Fit this KNN model to the training data.**

# %%


# %% [markdown]
# # Predictions and Evaluations
# Let's evaluate our KNN model!

# %% [markdown]
# **Use the predict method to predict values using your KNN model and X_test.**

# %%


# %% [markdown]
# ** Create a confusion matrix and classification report.**

# %%


# %%


# %%


# %% [markdown]
# # Choosing a K Value
# Let's go ahead and use the elbow method to pick a good K Value!
#
# ** Create a for loop that trains various KNN models with different k values, then keep track of the error_rate for each of these models with a list. Refer to the lecture if you are confused on this step.**

# %%


# %% [markdown]
# **Now create the following plot using the information from your for loop.**

# %%


# %% [markdown]
# ## Retrain with new K Value
#
# **Retrain your model with the best K value (up to you to decide what you want) and re-do the classification report and the confusion matrix.**

# %%
