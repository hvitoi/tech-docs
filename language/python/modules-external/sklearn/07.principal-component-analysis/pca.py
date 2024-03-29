# %% [markdown]
# # Principal Component Analysis
#
# Let's discuss PCA! Since this isn't exactly a full machine learning algorithm, but instead an unsupervised learning algorithm, we will just have a lecture on this topic, but no full machine learning project (although we will walk through the cancer set with PCA).
#
# ## PCA Review
#
# Make sure to watch the video lecture and theory presentation for a full overview of PCA!
# Remember that PCA is just a transformation of your data and attempts to find out what features explain the most variance in your data. For example:

# %% [markdown]
# <img src='PCA.png' />

# %% [markdown]
# ## Libraries

# %%
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
%matplotlib inline

# %% [markdown]
# ## The Data
#
# Let's work with the cancer data set again since it had so many features.

# %%
from sklearn.datasets import load_breast_cancer

# %%
cancer = load_breast_cancer()

# %%
cancer.keys()

# %%
print(cancer['DESCR'])

# %%
df = pd.DataFrame(cancer['data'],columns=cancer['feature_names'])
#(['DESCR', 'data', 'feature_names', 'target_names', 'target'])

# %%
df.head()

# %% [markdown]
# ## PCA Visualization
#
# As we've noticed before it is difficult to visualize high dimensional data, we can use PCA to find the first two principal components, and visualize the data in this new, two-dimensional space, with a single scatter-plot. Before we do this though, we'll need to scale our data so that each feature has a single unit variance.

# %%
from sklearn.preprocessing import StandardScaler

# %%
scaler = StandardScaler()
scaler.fit(df)

# %%
scaled_data = scaler.transform(df)

# %% [markdown]
# PCA with Scikit Learn uses a very similar process to other preprocessing functions that come with SciKit Learn. We instantiate a PCA object, find the principal components using the fit method, then apply the rotation and dimensionality reduction by calling transform().
#
# We can also specify how many components we want to keep when creating the PCA object.

# %%
from sklearn.decomposition import PCA

# %%
pca = PCA(n_components=2)

# %%
pca.fit(scaled_data)

# %% [markdown]
# Now we can transform this data to its first 2 principal components.

# %%
x_pca = pca.transform(scaled_data)

# %%
scaled_data.shape

# %%
x_pca.shape

# %% [markdown]
# Great! We've reduced 30 dimensions to just 2! Let's plot these two dimensions out!

# %%
plt.figure(figsize=(8,6))
plt.scatter(x_pca[:,0],x_pca[:,1],c=cancer['target'],cmap='plasma')
plt.xlabel('First principal component')
plt.ylabel('Second Principal Component')

# %% [markdown]
# Clearly by using these two components we can easily separate these two classes.
#
# ## Interpreting the components
#
# Unfortunately, with this great power of dimensionality reduction, comes the cost of being able to easily understand what these components represent.
#
# The components correspond to combinations of the original features, the components themselves are stored as an attribute of the fitted PCA object:

# %%
pca.components_

# %% [markdown]
# In this numpy matrix array, each row represents a principal component, and each column relates back to the original features. we can visualize this relationship with a heatmap:

# %%
df_comp = pd.DataFrame(pca.components_,columns=cancer['feature_names'])
df_comp

# %%
plt.figure(figsize=(12,6))
sns.heatmap(df_comp,cmap='plasma',)

# %% [markdown]
# This heatmap and the color bar basically represent the correlation between the various feature and the principal component itself.
#
# ## Conclusion
#
# Hopefully this information is useful to you when dealing with high dimensional data!


