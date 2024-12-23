# %% [markdown]
# ## The Data
#
# We will be working with a famous titanic data set for these exercises. Later on in the Machine Learning section of the course, we will revisit this data, and use it to predict survival rates of passengers. For now, we'll just focus on the visualization of the data with seaborn:

# %%
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

# %%
sns.set_style('whitegrid')

# %%
titanic = sns.load_dataset('titanic')

# %%
titanic.head(20)

# %% [markdown]
# # Exercises
#
# ** Recreate the plots below using the titanic dataframe. There are very few hints since most of the plots can be done with just one or two lines of code and a hint would basically give away the solution. Keep careful attention to the x and y labels for hints.**
#
# ** *Note! In order to not lose the plot image, make sure you don't code in the cell that is directly above the plot, there is an extra cell above that one which won't overwrite that plot!* **

# %%
sns.jointplot(data=titanic, x='fare', y='age')

# %%


# %%
sns.distplot(titanic['fare'],kde=False, bins=30)

# %%


# %%
sns.boxplot(data=titanic, x='class', y='age')

# %%


# %%
sns.swarmplot(data=titanic,x='class', y='age')

# %%


# %%
sns.countplot(data=titanic, x='sex')

# %%


# %%
sns.heatmap(titanic.corr(), cmap='coolwarm')
plt.title('titanic.corr()')

# %%
g = sns.FacetGrid(data=titanic, col='sex')
g.map(plt.hist,'age')

# %%



