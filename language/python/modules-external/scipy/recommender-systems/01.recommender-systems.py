# %% [markdown]
# # Recommender Systems
#
# Welcome to the code notebook for Recommender Systems with Python. In this lecture we will develop basic recommendation systems using Python and pandas. There is another notebook: *Advanced Recommender Systems with Python*. That notebook goes into more detail with the same data set.
#
# In this notebook, we will focus on providing a basic recommendation system by suggesting items that are most similar to a particular item, in this case, movies. Keep in mind, this is not a true robust recommendation system, to describe it more accurately,it just tells you what movies/items are most similar to your movie choice.
#
# There is no project for this topic, instead you have the option to work through the advanced lecture version of this notebook (totally optional!).
#
# Let's get started!
#
# ## Import Libraries

# %%
import numpy as np
import pandas as pd

# %% [markdown]
# ## Get the Data

# %%
column_names = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('u.data', sep='\t', names=column_names)

# %%
df.head()

# %% [markdown]
# Now let's get the movie titles:

# %%
movie_titles = pd.read_csv("Movie_Id_Titles")
movie_titles.head()

# %% [markdown]
# We can merge them together:

# %%
df = pd.merge(df,movie_titles,on='item_id')
df.head()

# %% [markdown]
# # EDA
#
# Let's explore the data a bit and get a look at some of the best rated movies.
#
# ## Visualization Imports

# %%
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')
%matplotlib inline

# %% [markdown]
# Let's create a ratings dataframe with average rating and number of ratings:

# %%
df.groupby('title').describe()

# %%
df.groupby('title')['rating'].mean().sort_values(ascending=False).head() #Filmes com "rating" maior

# %%
df.groupby('title')['rating'].count().sort_values(ascending=False).head() #Filmes com mais "ratings"

# %%
ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings.head()

# %% [markdown]
# Now set the number of ratings column:

# %%
ratings['num of ratings'] = df.groupby('title')['rating'].count()
ratings.head()

# %%
ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())
ratings.head()

# %%
ratings.loc['Star Wars (1977)']

# %% [markdown]
# Now a few histograms:

# %%
plt.figure(figsize=(10,4))
ratings['num of ratings'].hist(bins=70)

# %%
plt.figure(figsize=(10,4))
ratings['rating'].hist(bins=70)

# %%
sns.jointplot(x='rating',y='num of ratings',data=ratings,alpha=0.5)

# %% [markdown]
# Okay! Now that we have a general idea of what the data looks like, let's move on to creating a simple recommendation system:

# %% [markdown]
# ## Recommending Similar Movies

# %% [markdown]
# Now let's create a matrix that has the user ids on one access and the movie title on another axis. Each cell will then consist of the rating the user gave to that movie. Note there will be a lot of NaN values, because most people have not seen most of the movies.

# %%
df.head()

# %%
moviemat = df.pivot_table(index='user_id',columns='title',values='rating')
moviemat.head()

# %% [markdown]
# Most rated movie:

# %%
ratings.sort_values('num of ratings',ascending=False).head(10)

# %% [markdown]
# Let's choose two movies: starwars, a sci-fi movie. And Liar Liar, a comedy.

# %%
ratings.head()

# %% [markdown]
# Now let's grab the user ratings for those two movies:

# %%
starwars_user_ratings = moviemat['Star Wars (1977)']
liarliar_user_ratings = moviemat['Liar Liar (1997)']
starwars_user_ratings.head()

# %% [markdown]
# We can then use corrwith() method to get correlations between two pandas series:

# %%
similar_to_starwars = moviemat.corrwith(starwars_user_ratings)
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)

# %% [markdown]
# Let's clean this by removing NaN values and using a DataFrame instead of a series:

# %%
corr_starwars = pd.DataFrame(similar_to_starwars,columns=['Correlation'])
corr_starwars.dropna(inplace=True)
corr_starwars.head()

# %% [markdown]
# Now if we sort the dataframe by correlation, we should get the most similar movies, however note that we get some results that don't really make sense. This is because there are a lot of movies only watched once by users who also watched star wars (it was the most popular movie).

# %%
corr_starwars.sort_values('Correlation',ascending=False).head(10)

# %% [markdown]
# Let's fix this by filtering out movies that have less than 100 reviews (this value was chosen based off the histogram from earlier).

# %%
corr_starwars = corr_starwars.join(ratings['num of ratings'])
corr_starwars.head()

# %% [markdown]
# Now sort the values and notice how the titles make a lot more sense:

# %%
corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation',ascending=False).head()

# %% [markdown]
# Now the same for the comedy Liar Liar:

# %%
corr_liarliar = pd.DataFrame(similar_to_liarliar,columns=['Correlation'])
corr_liarliar.dropna(inplace=True)
corr_liarliar = corr_liarliar.join(ratings['num of ratings'])
corr_liarliar[corr_liarliar['num of ratings']>100].sort_values('Correlation',ascending=False).head()


