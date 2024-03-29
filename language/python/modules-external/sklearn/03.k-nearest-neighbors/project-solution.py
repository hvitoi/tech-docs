# %% [markdown]
# # K Nearest Neighbors Project - Solution
#
# Welcome to the KNN Project! This will be a simple project very similar to the lecture, except you'll be given another data set. Go ahead and just follow the directions below.
# ## Import Libraries
# **Import pandas,seaborn, and the usual libraries.**

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

# %% [markdown]
# ## Get the Data
# ** Read the 'KNN_Project_Data csv file into a dataframe **

# %%
df = pd.read_csv('KNN_Project_Data')

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
# THIS IS GOING TO BE A VERY LARGE PLOT
sns.pairplot(df,hue='TARGET CLASS',palette='coolwarm')

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
scaler.fit(df.drop('TARGET CLASS',axis=1))

# %% [markdown]
# **Use the .transform() method to transform the features to a scaled version.**

# %%
scaled_features = scaler.transform(df.drop('TARGET CLASS',axis=1))

# %% [markdown]
# **Convert the scaled features to a dataframe and check the head of this dataframe to make sure the scaling worked.**

# %%
df_feat = pd.DataFrame(scaled_features,columns=df.columns[:-1])
df_feat.head()

# %% [markdown]
# # Train Test Split
#
# **Use train_test_split to split your data into a training set and a testing set.**

# %%
from sklearn.model_selection import train_test_split

# %%
X_train, X_test, y_train, y_test = train_test_split(scaled_features,df['TARGET CLASS'],
                                                    test_size=0.30)

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
knn.fit(X_train,y_train)

# %% [markdown]
# # Predictions and Evaluations
# Let's evaluate our KNN model!

# %% [markdown]
# **Use the predict method to predict values using your KNN model and X_test.**

# %%
pred = knn.predict(X_test)

# %% [markdown]
# ** Create a confusion matrix and classification report.**

# %%
from sklearn.metrics import classification_report,confusion_matrix

# %%
print(confusion_matrix(y_test,pred))

# %%
print(classification_report(y_test,pred))

# %% [markdown]
# # Choosing a K Value
# Let's go ahead and use the elbow method to pick a good K Value!
#
# ** Create a for loop that trains various KNN models with different k values, then keep track of the error_rate for each of these models with a list. Refer to the lecture if you are confused on this step.**

# %%
error_rate = []

# Will take some time
for i in range(1,40):

    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))

# %% [markdown]
# **Now create the following plot using the information from your for loop.**

# %%
plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate,color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')

# %% [markdown]
# ## Retrain with new K Value
#
# **Retrain your model with the best K value (up to you to decide what you want) and re-do the classification report and the confusion matrix.**

# %%
# NOW WITH K=30
knn = KNeighborsClassifier(n_neighbors=30)

knn.fit(X_train,y_train)
pred = knn.predict(X_test)

print('WITH K=30')
print('\n')
print(confusion_matrix(y_test,pred))
print('\n')
print(classification_report(y_test,pred))


