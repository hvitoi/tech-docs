# %% [markdown]
# # K Nearest Neighbors with Python
#
# You've been given a classified data set from a company! They've hidden the feature column names but have given you the data and the target classes.
#
# We'll try to use KNN to create a model that directly predicts a class for a new data point based off of the features.
#
# Let's grab it and use it!

# %% [markdown]
# ## Import Libraries
#
#

# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

# %% [markdown]
# ## Get the Data
#
# Set index_col=0 to use the first column as the index.

# %%
df = pd.read_csv("Classified Data",index_col=0)

# %%
df.head()

# %%


# %% [markdown]
# ## Standardize the Variables
#
# Because the KNN classifier predicts the class of a given test observation by identifying the observations that are nearest to it, the scale of the variables matters. Any variables that are on a large scale will have a much larger effect on the distance between the observations, and hence on the KNN classifier, than variables that are on a small scale.

# %%
from sklearn.preprocessing import StandardScaler

# %%
scaler = StandardScaler()

# %%
scaler.fit(df.drop('TARGET CLASS',axis=1))

# %%
scaled_features = scaler.transform(df.drop('TARGET CLASS',axis=1))

# %%
df_feat = pd.DataFrame(scaled_features,columns=df.columns[:-1]) #Columns: Everything but the last one
df_feat.head()

# %% [markdown]
# ## Train Test Split

# %%
from sklearn.model_selection import train_test_split

# %%
X = scaled_features
y = df['TARGET CLASS']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)

# %% [markdown]
# ## Using KNN
#
# Remember that we are trying to come up with a model to predict whether someone will TARGET CLASS or not. We'll start with k=1.

# %%
from sklearn.neighbors import KNeighborsClassifier

# %%
knn = KNeighborsClassifier(n_neighbors=1)

# %%
knn.fit(X_train,y_train)

# %%
pred = knn.predict(X_test)

# %% [markdown]
# ## Predictions and Evaluations
#
# Let's evaluate our KNN model!

# %%
from sklearn.metrics import classification_report,confusion_matrix

# %%
print(confusion_matrix(y_test,pred))

# %%
print(classification_report(y_test,pred))

# %%
np.mean(pred != y_test)

# %%


# %% [markdown]
# ## Choosing a K Value
#
# Let's go ahead and use the elbow method to pick a good K Value:

# %%
error_rate = []

# Will take some time
for i in range(1,40):

    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test)) # "pred_i != y_test" retorna Series com True e False "np.mean()" tira a média de "predições erradas/predições certas"

# %%
plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate,color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')

# %% [markdown]
# Here we can see that that after arouns K>23 the error rate just tends to hover around 0.06-0.05 Let's retrain the model with that and check the classification report!

# %%
# FIRST A QUICK COMPARISON TO OUR ORIGINAL K=1
knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train,y_train)
pred = knn.predict(X_test)

print('WITH K=1')
print('\n')
print(confusion_matrix(y_test,pred))
print('\n')
print(classification_report(y_test,pred))

# %%
# NOW WITH K=23
knn = KNeighborsClassifier(n_neighbors=23)

knn.fit(X_train,y_train)
pred = knn.predict(X_test)

print('WITH K=23')
print('\n')
print(confusion_matrix(y_test,pred))
print('\n')
print(classification_report(y_test,pred))

# %% [markdown]
# We were able to squeeze some more performance out of our model by tuning to a better K value!


