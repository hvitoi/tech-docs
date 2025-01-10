# %% [markdown]
# # Choropleth Maps Exercise
#
# Welcome to the Choropleth Maps Exercise! In this exercise we will give you some simple datasets and ask you to create Choropleth Maps from them. Due to the Nature of Plotly we can't show you examples
#
# [Full Documentation Reference](https://plot.ly/python/reference/#choropleth)
#
# ## Plotly Imports

# %%
import plotly.graph_objs as go
# from plotly.offline import init_notebook_mode,iplot
# init_notebook_mode(connected=True)

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
    locationmode="country names",
    locations=df["Country"],
    z=df["Power Consumption KWH"],
    # text = df['Country'],
    colorbar={"title": "Power Consumption (kWh)"},
)

layout = dict(
    title="2014 World Power Consumption",
    geo=dict(showframe=False, projection={"type": "natural earth"}),
)

# %%
power = go.Figure(data=[data], layout=layout)
power.show()

# %% [markdown]
# ## USA Choropleth
#
# ** Import the 2012_Election_Data csv file using pandas. **

# %%
df2 = pd.read_csv("2012_Election_Data")

# %% [markdown]
# ** Check the head of the DataFrame. **

# %%
df2.head()

# %% [markdown]
# ** Now create a plot that displays the Voting-Age Population (VAP) per state. If you later want to play around with other columns, make sure you consider their data type. VAP has already been transformed to a float for you. **

# %%
data = dict(
    type="choropleth",
    # colorscale = 'Jet',
    locationmode="USA-states",
    locations=df2["State Abv"],
    z=df2["Voting-Age Population (VAP)"],
    # text = df2['State'],
    colorbar={"title": "VAP"},
)

layout = dict(
    title="2012 Election Data",
    geo=dict(scope="usa", showlakes=True, lakecolor="rgb(85,173,240)"),
)


# %%
election = go.Figure(data=[data], layout=layout)
election.show()
