# %%
import pandas as pd
import matplotlib.pyplot as plt
df3 = pd.read_csv('df3')
%matplotlib inline

# %%
df3.info()

# %%
df3.head()

# %% [markdown]
# ** Recreate this scatter plot of b vs a. Note the color and size of the points. Also note the figure size. See if you can figure out how to stretch it in a similar fashion. Remeber back to your matplotlib lecture...**

# %%
df3.plot.scatter(x='a', y='b', figsize=(12,3), c='red', s=50)

# %% [markdown]
# ** Create a histogram of the 'a' column.**

# %%
df3['a'].plot.hist()

# %%


# %% [markdown]
# ** These plots are okay, but they don't look very polished. Use style sheets to set the style to 'ggplot' and redo the histogram from above. Also figure out how to add more bins to it.***

# %%
plt.style.use('ggplot')
df3['a'].plot.hist(bins=25, alpha=0.5)

# %%


# %% [markdown]
# ** Create a boxplot comparing the a and b columns.**

# %%
df3[['a','b']].plot.box()

# %%


# %% [markdown]
# ** Create a kde plot of the 'd' column **

# %%
df3['d'].plot.kde()

# %%


# %% [markdown]
# ** Figure out how to increase the linewidth and make the linestyle dashed. (Note: You would usually not dash a kde plot line)**

# %%
df3['d'].plot.density(lw=5,ls='--')

# %%


# %% [markdown]
# ** Create an area plot of all the columns for just the rows up to 30. (hint: use .ix).**

# %%
df3.iloc[0:30].plot.area()

# %%


# %% [markdown]
# ## Bonus Challenge!
# Note, you may find this really hard, reference the solutions if you can't figure it out!
# ** Notice how the legend in our previous figure overlapped some of actual diagram. Can you figure out how to display the legend outside of the plot as shown below?**
#
# ** Try searching Google for a good stackoverflow link on this topic. If you can't find it on your own - [use this one for a hint.](http://stackoverflow.com/questions/23556153/how-to-put-legend-outside-the-plot-with-pandas)**

# %%
df3.iloc[0:30].plot.area(alpha=0.4)


# %%



