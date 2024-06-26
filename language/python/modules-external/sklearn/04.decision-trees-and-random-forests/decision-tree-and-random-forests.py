# %% [markdown]
# This is the code for the lecture video which goes over tree methods in Python. Reference the video lecture for the full explanation of the code!
#
# I also wrote a [blog post](https://medium.com/@josemarcialportilla/enchanted-random-forest-b08d418cb411#.hh7n1co54) explaining the general logic of decision trees and random forests which you can check out.
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

# %%
df = pd.read_csv('kyphosis.csv')

# %%
df.head()

# %% [markdown]
# ## EDA
#
# We'll just check out a simple pairplot for this small dataset.

# %%
sns.pairplot(df,hue='Kyphosis', diag_kind='hist', palette='Set1')

# %% [markdown]
# ## Train Test Split
#
# Let's split up the data into a training set and a test set!

# %%
from sklearn.model_selection import train_test_split

# %%
X = df.drop('Kyphosis',axis=1)
y = df['Kyphosis']

# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)

# %% [markdown]
# ## Decision Trees
#
# We'll start just by training a single decision tree.

# %%
from sklearn.tree import DecisionTreeClassifier

# %%
dtree = DecisionTreeClassifier()

# %%
dtree.fit(X_train,y_train)

# %% [markdown]
# ## Prediction and Evaluation
#
# Let's evaluate our decision tree.

# %%
predictions = dtree.predict(X_test)

# %%
from sklearn.metrics import classification_report,confusion_matrix

# %%
print(classification_report(y_test,predictions))

# %%
print(classification_report(y_true=y_test, y_pred=predictions))

# %%
print(confusion_matrix(y_test,predictions))

# %% [markdown]
# ## Tree Visualization
#
# Scikit learn actually has some built-in visualization capabilities for decision trees, you won't use this often and it requires you to install the pydot library, but here is an example of what it looks like and the code to execute this:

# %%
from IPython.display import Image
from sklearn.externals.six import StringIO
from sklearn.tree import export_graphviz
import pydot

features = list(df.columns[1:])
features

# %%
dot_data = StringIO()
export_graphviz(dtree, out_file=dot_data,feature_names=features,filled=True,rounded=True)

graph = pydot.graph_from_dot_data(dot_data.getvalue())
Image(graph[0].create_png())  # http://www.graphviz.org/ Download graphviz in order to run the code

# %% [markdown]
# ## Random Forests
#
# Now let's compare the decision tree model to a random forest.

# %%
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=100)
rfc.fit(X_train, y_train)

# %%
rfc_pred = rfc.predict(X_test)

# %%
print(confusion_matrix(y_test,rfc_pred))

# %%
print(classification_report(y_test,rfc_pred))


