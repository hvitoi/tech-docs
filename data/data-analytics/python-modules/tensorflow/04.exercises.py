# %% [markdown]
# # Tensorflow Project Exercise
# Let's wrap up this Deep Learning by taking a a quick look at the effectiveness of Neural Nets!
#
# We'll use the [Bank Authentication Data Set](https://archive.ics.uci.edu/ml/datasets/banknote+authentication) from the UCI repository.
#
# The data consists of 5 columns:
#
# * variance of Wavelet Transformed image (continuous)
# * skewness of Wavelet Transformed image (continuous)
# * curtosis of Wavelet Transformed image (continuous)
# * entropy of image (continuous)
# * class (integer)
#
# Where class indicates whether or not a Bank Note was authentic.
#
# This sort of task is perfectly suited for Neural Networks and Deep Learning! Just follow the instructions below to get started!

# %% [markdown]
# ## Get the Data
#
# ** Use pandas to read in the bank_note_data.csv file **

# %%


# %%


# %% [markdown]
# ** Check the head of the Data **

# %%


# %% [markdown]
# ## EDA
#
# We'll just do a few quick plots of the data.
#
# ** Import seaborn and set matplolib inline for viewing **

# %%


# %% [markdown]
# ** Create a Countplot of the Classes (Authentic 1 vs Fake 0) **

# %%


# %% [markdown]
# ** Create a PairPlot of the Data with Seaborn, set Hue to Class **

# %%


# %% [markdown]
# ## Data Preparation
#
# When using Neural Network and Deep Learning based systems, it is usually a good idea to Standardize your data, this step isn't actually necessary for our particular data set, but let's run through it for practice!
#
# ### Standard Scaling
#
#

# %%


# %% [markdown]
# **Create a StandardScaler() object called scaler.**

# %%


# %% [markdown]
# **Fit scaler to the features.**

# %%


# %% [markdown]
# **Use the .transform() method to transform the features to a scaled version.**

# %%


# %% [markdown]
# **Convert the scaled features to a dataframe and check the head of this dataframe to make sure the scaling worked.**

# %%


# %% [markdown]
# ## Train Test Split
#
# ** Create two objects X and y which are the scaled feature values and labels respectively.**

# %%


# %%


# %% [markdown]
# ** Use SciKit Learn to create training and testing sets of the data as we've done in previous lectures:**

# %%


# %%


# %% [markdown]
# # Tensorflow

# %%


# %% [markdown]
# ** Create a list of feature column objects using tf.feature.numeric_column() as we did in the lecture**

# %%


# %%


# %%


# %% [markdown]
# ** Create an object called classifier which is a DNNClassifier from learn. Set it to have 2 classes and a [10,20,10] hidden unit layer structure:**

# %%


# %% [markdown]
# ** Now create a tf.estimator.pandas_input_fn that takes in your X_train, y_train, batch_size and set shuffle=True. You can play around with the batch_size parameter if you want, but let's start by setting it to 20 since our data isn't very big. **

# %%


# %% [markdown]
# ** Now train classifier to the input function. Use steps=500. You can play around with these values if you want!**
#
# *Note: Ignore any warnings you get, they won't effect your output*

# %%


# %% [markdown]
# ## Model Evaluation

# %% [markdown]
# ** Create another pandas_input_fn that takes in the X_test data for x. Remember this one won't need any y_test info since we will be using this for the network to create its own predictions. Set shuffle=False since we don't need to shuffle for predictions.**

# %%


# %% [markdown]
# ** Use the predict method from the classifier model to create predictions from X_test **

# %%


# %%


# %%


# %% [markdown]
# ** Now create a classification report and a Confusion Matrix. Does anything stand out to you?**

# %%


# %%


# %%


# %% [markdown]
# ## Optional Comparison
#
# ** You should have noticed extremely accurate results from the DNN model. Let's compare this to a Random Forest Classifier for a reality check!**
#
# **Use SciKit Learn to Create a Random Forest Classifier and compare the confusion matrix and classification report to the DNN model**

# %%


# %%


# %%


# %%


# %%


# %%


# %% [markdown]
# ** It should have also done very well, possibly perfect! Hopefully you have seen the power of DNN! **


