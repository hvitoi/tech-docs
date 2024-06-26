# %% [markdown]
# # Choropleth Maps Exercise - Solutions
#
# Welcome to the Choropleth Maps Exercise! In this exercise we will give you some simple datasets and ask you to create Choropleth Maps from them. Due to the Nature of Plotly we can't show you examples embedded inside the notebook.
#
# [Full Documentation Reference](https://plot.ly/python/reference/#choropleth)
#
# ## Plotly Imports

# %%
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot, plot

init_notebook_mode(connected=True)

# %% [markdown]
# ** Import pandas and read the csv file: 2014_World_Power_Consumption**

# %%
import pandas as pd

# %%
df = pd.read_csv("2014_World_Power_Consumption")

# %% [markdown]
# ** Check the head of the DataFrame. **

# %%
df.head()

# %% [markdown]
# ** Referencing the lecture notes, create a Choropleth Plot of the Power Consumption for Countries using the data and layout dictionary. **

# %%
data = dict(
    type="choropleth",
    colorscale="Viridis",
    reversescale=True,
    locations=df["Country"],
    locationmode="country names",
    z=df["Power Consumption KWH"],
    text=df["Country"],
    colorbar={"title": "Power Consumption KWH"},
)

layout = dict(
    title="2014 Power Consumption KWH",
    geo=dict(showframe=False, projection={"type": "Mercator"}),
)

# %%
choromap = go.Figure(data=[data], layout=layout)
plot(choromap, validate=False)

# %% [markdown]
# ## USA Choropleth
#
# ** Import the 2012_Election_Data csv file using pandas. **

# %%
usdf = pd.read_csv("2012_Election_Data")

# %% [markdown]
# ** Check the head of the DataFrame. **

# %%
usdf.head()

# %% [markdown]
# ** Now create a plot that displays the Voting-Age Population (VAP) per state. If you later want to play around with other columns, make sure you consider their data type. VAP has already been transformed to a float for you. **

# %%
data = dict(
    type="choropleth",
    colorscale="Viridis",
    reversescale=True,
    locations=usdf["State Abv"],
    z=usdf["Voting-Age Population (VAP)"],
    locationmode="USA-states",
    text=usdf["State"],
    marker=dict(line=dict(color="rgb(255,255,255)", width=1)),
    colorbar={"title": "Voting-Age Population (VAP)"},
)

# %%
layout = dict(
    title="2012 General Election Voting Data",
    geo=dict(scope="usa", showlakes=True, lakecolor="rgb(85,173,240)"),
)

# %%
choromap = go.Figure(data=[data], layout=layout)
plot(choromap, validate=False)
