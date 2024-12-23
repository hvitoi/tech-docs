# %% [markdown]
# # Support Vector Machines
#
# Welcome to the Support Vector Machines with Python Lecture Notebook! Remember to refer to the video lecture for the full background information on the code here!
#
# ## Import Libraries

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

# %% [markdown]
# ## Get the Data
#
# We'll use the built in breast cancer dataset from Scikit Learn. We can get with the load function:

# %%
from sklearn.datasets import load_breast_cancer

# %%
cancer = load_breast_cancer()

# %% [markdown]
# The data set is presented in a dictionary form:

# %%
cancer.keys()

# %%



# %% [markdown]
# We can grab information and arrays out of this dictionary to set up our data frame and understanding of the features:

# %%
print(cancer['DESCR'])

# %%
cancer['feature_names']

# %% [markdown]
# ## Set up DataFrame

# %%
df_feat = pd.DataFrame(cancer['data'],columns=cancer['feature_names'])
df_feat.info()

# %%
cancer['target']

# %%
df_target = pd.DataFrame(cancer['target'],columns=['Cancer'])

# %%
df_target

# %% [markdown]
# Now let's actually check out the dataframe!

# %%
np.ravel(df_target)

# %% [markdown]
# # Exploratory Data Analysis
#
#

# %% [markdown]
# We'll skip the Data Viz part for this lecture since there are so many features that are hard to interpret if you don't have domain knowledge of cancer or tumor cells. In your project you will have more to visualize for the data.

# %% [markdown]
# ## Train Test Split

# %%
from sklearn.model_selection import train_test_split

# %%
X_train, X_test, y_train, y_test = train_test_split(df_feat, df_target, test_size=0.30, random_state=101)

# %% [markdown]
# # Train the Support Vector Classifier

# %%
from sklearn.svm import SVC

# %%
model = SVC()

# %%
model.fit(X_train,y_train)

# %% [markdown]
# ## Predictions and Evaluations
#
# Now let's predict using the trained model.

# %%
predictions = model.predict(X_test)

# %%
from sklearn.metrics import classification_report,confusion_matrix

# %%
print(confusion_matrix(y_test,predictions))

# %%
print(classification_report(y_test,predictions))

# %% [markdown]
# Woah! Notice that we are classifying everything into a single class! This means our model needs to have it parameters adjusted (it may also help to normalize the data).
#
# We can search for parameters using a GridSearch!

# %% [markdown]
# # Gridsearch
#
# Finding the right parameters (like what C or gamma values to use) is a tricky task! But luckily, we can be a little lazy and just try a bunch of combinations and see what works best! This idea of creating a 'grid' of parameters and just trying out all the possible combinations is called a Gridsearch, this method is common enough that Scikit-learn has this functionality built in with GridSearchCV! The CV stands for cross-validation which is the
#
# GridSearchCV takes a dictionary that describes the parameters that should be tried and a model to train. The grid of parameters is defined as a dictionary, where the keys are the parameters and the values are the settings to be tested.

# %%
param_grid = {'C': [0.1,1, 10, 100, 1000], 'gamma': [1,0.1,0.01,0.001,0.0001], 'kernel': ['rbf']}

# %%
from sklearn.model_selection import GridSearchCV

# %% [markdown]
# One of the great things about GridSearchCV is that it is a meta-estimator. It takes an estimator like SVC, and creates a new estimator, that behaves exactly the same - in this case, like a classifier. You should add refit=True and choose verbose to whatever number you want, higher the number, the more verbose (verbose just means the text output describing the process).

# %%
grid = GridSearchCV(SVC(),param_grid,refit=True,verbose=3)

# %% [markdown]
# What fit does is a bit more involved then usual. First, it runs the same loop with cross-validation, to find the best parameter combination. Once it has the best combination, it runs fit again on all data passed to fit (without cross-validation), to built a single new model using the best parameter setting.

# %%
# May take awhile!
grid.fit(X_train,y_train)

# %% [markdown]
# You can inspect the best parameters found by GridSearchCV in the best_params_ attribute, and the best estimator in the best\_estimator_ attribute:

# %%
grid.best_params_

# %%
grid.best_estimator_

# %% [markdown]
# Then you can re-run predictions on this grid object just like you would with a normal model.

# %%
grid_predictions = grid.predict(X_test)

# %%
print(confusion_matrix(y_test,grid_predictions))

# %%
print(classification_report(y_test,grid_predictions))


