# %% [markdown]
# ## Check out the data
# We've been able to get some data from your neighbor for housing prices as a csv set, let's get our environment ready with the libraries we'll need and then import the data!
# ### Import Libraries

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

# %% [markdown]
# ### Check out the Data

# %%
USAhousing = pd.read_csv('USA_Housing.csv')

# %%
USAhousing.head()

# %%
USAhousing.info()

# %%
USAhousing.describe()

# %%
USAhousing.columns

# %% [markdown]
# # EDA
#
# Let's create some simple plots to check out the data!

# %%
sns.pairplot(USAhousing)

# %%
sns.distplot(USAhousing['Price'])

# %%
sns.heatmap(USAhousing.corr())

# %% [markdown]
# ## Training a Linear Regression Model
#
# Let's now begin to train out regression model! We will need to first split up our data into an X array that contains the features to train on, and a y array with the target variable, in this case the Price column. We will toss out the Address column because it only has text info that the linear regression model can't use.
#
# ### X and y arrays

# %%
X = USAhousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
               'Avg. Area Number of Bedrooms', 'Area Population']] # Features to train
y = USAhousing['Price'] # Target variable - What I'm trying to predict

# %% [markdown]
# ## Train Test Split
#
# Now let's split the data into a training set and a testing set. We will train out model on the training set and then use the test set to evaluate the model.

# %%
from sklearn.model_selection import train_test_split

# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

# %%
pd.concat([X_train,y_train], axis=1).head() #df de treino

# %%
pd.concat([X_test,y_test], axis=1).head() #df de teste

# %% [markdown]
# ## Creating and Training the Model

# %%
from sklearn.linear_model import LinearRegression

# %%
lm = LinearRegression()

# %%
lm.fit(X_train,y_train) #Fit my model or my training data

# %% [markdown]
# ## Model Evaluation
#
# Let's evaluate the model by checking out it's coefficients and how we can interpret them.

# %%
# print the intercept
print(lm.intercept_)

# %%
coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])
coeff_df

# %% [markdown]
# Interpreting the coefficients:
#
# - Holding all other features fixed, a 1 unit increase in **Avg. Area Income** is associated with an **increase of \$21.52 **.
# - Holding all other features fixed, a 1 unit increase in **Avg. Area House Age** is associated with an **increase of \$164883.28 **.
# - Holding all other features fixed, a 1 unit increase in **Avg. Area Number of Rooms** is associated with an **increase of \$122368.67 **.
# - Holding all other features fixed, a 1 unit increase in **Avg. Area Number of Bedrooms** is associated with an **increase of \$2233.80 **.
# - Holding all other features fixed, a 1 unit increase in **Area Population** is associated with an **increase of \$15.15 **.
#
# Does this make sense? Probably not because I made up this data. If you want real data to repeat this sort of analysis, check out the [boston dataset](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html):
#
#

# %%
from sklearn.datasets import load_boston
boston = load_boston()
boston_features = pd.DataFrame(data=boston['data'], columns=boston['feature_names'])
boston_target = pd.DataFrame(data=boston['target'], columns=['Price'])
boston_df = pd.concat([boston_features, boston_target],axis=1)
boston_df

# %%
X_boston_train, X_boston_test, y_boston_train, y_boston_test = train_test_split(boston_features, boston_target, test_size=0.4)

# %%
boston_lm = LinearRegression()

# %%
boston_lm.fit(X_boston_train, y_boston_train)

# %%
boston_lm.coef_

# %%
array(boston_features.columns)

# %%
coeff_df = pd.DataFrame(data=boston_lm.coef_, index=[boston_features.columns], columns=['Coefficient'])
coeff_df

# %% [markdown]
# ## Predictions from our Model
#
# Let's grab predictions off our test set and see how well it did!

# %%
predictions = lm.predict(X_test)

# %%
predictions

# %%
plt.scatter(y_test,predictions)

# %% [markdown]
# **Residual Histogram**

# %%
sns.distplot((y_test-predictions),bins=50);

# %% [markdown]
# ## Regression Evaluation Metrics
#
#
# Here are three common evaluation metrics for regression problems:
#
# **Mean Absolute Error** (MAE) is the mean of the absolute value of the errors:
#
# $$\frac 1n\sum_{i=1}^n|y_i-\hat{y}_i|$$
#
# **Mean Squared Error** (MSE) is the mean of the squared errors:
#
# $$\frac 1n\sum_{i=1}^n(y_i-\hat{y}_i)^2$$
#
# **Root Mean Squared Error** (RMSE) is the square root of the mean of the squared errors:
#
# $$\sqrt{\frac 1n\sum_{i=1}^n(y_i-\hat{y}_i)^2}$$
#
# Comparing these metrics:
#
# - **MAE** is the easiest to understand, because it's the average error.
# - **MSE** is more popular than MAE, because MSE "punishes" larger errors, which tends to be useful in the real world.
# - **RMSE** is even more popular than MSE, because RMSE is interpretable in the "y" units.
#
# All of these are **loss functions**, because we want to minimize them.

# %%
from sklearn import metrics

# %%
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

# %% [markdown]
# Bias-variance tradeoff
#
# Bias (Erro sistemático): Mudança do centro
# Variance (Erro aleatório): Mudança da dispersão


