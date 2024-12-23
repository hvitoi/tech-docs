# %% [markdown]
# # Style and Color
#
# We've shown a few times how to control figure aesthetics in seaborn, but let's now go over it formally:

# %%
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
tips = sns.load_dataset('tips')

# %% [markdown]
# ## Styles
#
# You can set particular styles:

# %%
sns.countplot(x='sex',data=tips)

# %%
sns.set_style('white')
sns.countplot(x='sex',data=tips)

# %%
sns.set_style('ticks')
sns.countplot(x='sex',data=tips,palette='deep')

# %% [markdown]
# ## Spine Removal

# %%
sns.countplot(x='sex',data=tips)
sns.despine()

# %%
sns.countplot(x='sex',data=tips)
sns.despine(left=True, bottom=True)

# %% [markdown]
# ## Size and Aspect

# %% [markdown]
# You can use matplotlib's **plt.figure(figsize=(width,height) ** to change the size of most seaborn plots.
#
# You can control the size and aspect ratio of most seaborn grid plots by passing in parameters: size, and aspect. For example:

# %%
# Non Grid Plot
plt.figure(figsize=(12,3))
sns.countplot(x='sex',data=tips)

# %%
# Grid Type Plot
sns.lmplot(x='total_bill',y='tip',size=2,aspect=4,data=tips)

# %% [markdown]
# ## Scale and Context
#
# The set_context() allows you to override default parameters:

# %%
sns.set_context('poster',font_scale=4)
sns.countplot(x='sex',data=tips,palette='coolwarm')

# %%
sns.set_context('notebook')
sns.countplot(x='sex',data=tips,palette='coolwarm')

# %% [markdown]
# Check out the documentation page for more info on these topics:
# https://stanford.edu/~mwaskom/software/seaborn/tutorial/aesthetics.html

# %%
sns.puppyplot()


