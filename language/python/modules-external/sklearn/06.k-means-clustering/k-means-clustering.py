# %% [markdown]
# # K Means Clustering with Python
#
# This notebook is just a code reference for the video lecture and reading.
#
# ## Method Used
#
# K Means Clustering is an unsupervised learning algorithm that tries to cluster data based on their similarity. Unsupervised learning means that there is no outcome to be predicted, and the algorithm just tries to find patterns in the data. In k means clustering, we have the specify the number of clusters we want the data to be grouped into. The algorithm randomly assigns each observation to a cluster, and finds the centroid of each cluster. Then, the algorithm iterates through two steps:
# Reassign data points to the cluster whose centroid is closest. Calculate new centroid of each cluster. These two steps are repeated till the within cluster variation cannot be reduced any further. The within cluster variation is calculated as the sum of the euclidean distance between the data points and their respective cluster centroids.

# %% [markdown]
# ## Import Libraries

# %%
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# %% [markdown]
# ## Create some Data

# %%
from sklearn.datasets import make_blobs

# %%
# Create Data
data = make_blobs(n_samples=200, n_features=2, centers=4, cluster_std=1.8,random_state=101)
data

# %%


# %%


# %% [markdown]
# ## Visualize Data

# %%
plt.scatter(data[0][:,0],data[0][:,1],c=data[1],cmap='rainbow')


# %% [markdown]
# ## Creating the Clusters

# %%
from sklearn.cluster import KMeans

# %%
kmeans = KMeans(n_clusters=4)

# %%
kmeans.fit(data[0])

# %%
kmeans.cluster_centers_

# %%
kmeans.labels_

# %%
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True,figsize=(10,6))
ax1.set_title('K Means')
ax1.scatter(data[0][:,0],data[0][:,1],c=kmeans.labels_,cmap='rainbow')
ax2.set_title("Original")
ax2.scatter(data[0][:,0],data[0][:,1],c=data[1],cmap='rainbow')

# %% [markdown]
# You should note, the colors are meaningless in reference between the two plots.


