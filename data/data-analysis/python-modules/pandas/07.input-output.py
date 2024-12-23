# %% [markdown]
# # Data Input and Output
#
# This notebook is the reference code for getting input and output, pandas can read a variety of file types using its pd.read_ methods. Let's take a look at the most common data types:

# %%
import numpy as np
import pandas as pd

# %% [markdown]
# ## CSV
#
# ### CSV Input

# %%
pwd

# %%
df = pd.read_csv("example")  # Ler
df

# %% [markdown]
# ### CSV Output

# %%
df.to_csv("example", index=False)  # Salvar. Index=False não salva o index na tabela

# %% [markdown]
# ## Excel
# Pandas can read and write excel files, keep in mind, this only imports data. Not formulas or images, having images or macros may cause this read_excel method to crash.

# %% [markdown]
# ### Excel Input

# %%
pd.read_excel("Excel_Sample.xlsx", sheetname="Sheet1")

# %%
pd.read_excel("Excel_Sample.xlsx", sheet_name=0)

# %%
pd.to_excel("Excel_sample2.xlsx", sheet_name=0)

# %% [markdown]
# ### Excel Output

# %% [markdown]
# ## HTML
#
# You may need to install htmllib5,lxml, and BeautifulSoup4. In your terminal/command prompt run:
#
#     conda install lxml
#     conda install html5lib
#     conda install BeautifulSoup4
#
# Then restart Jupyter Notebook.
# (or use pip install if you aren't using the Anaconda Distribution)
#
# Pandas can read table tabs off of html. For example:

# %% [markdown]
# ### HTML Input
#
# Pandas read_html function will read tables off of a webpage and return a list of DataFrame objects:

# %%
df = pd.read_html("http://www.fdic.gov/bank/individual/failed/banklist.html")

# %%
type(df)

# %%
df

# %%
df = df[0]

# %% [markdown]
# ____

# %% [markdown]
# _____
# _____
# # SQL (Optional)
#
# * Note: If you are completely unfamiliar with SQL you can check out my other course: "Complete SQL Bootcamp" to learn SQL.

# %% [markdown]
# The pandas.io.sql module provides a collection of query wrappers to both facilitate data retrieval and to reduce dependency on DB-specific API. Database abstraction is provided by SQLAlchemy if installed. In addition you will need a driver library for your database. Examples of such drivers are psycopg2 for PostgreSQL or pymysql for MySQL. For SQLite this is included in Python’s standard library by default. You can find an overview of supported drivers for each SQL dialect in the SQLAlchemy docs.
#
#
# If SQLAlchemy is not installed, a fallback is only provided for sqlite (and for mysql for backwards compatibility, but this is deprecated and will be removed in a future version). This mode requires a Python database adapter which respect the Python DB-API.
#
# See also some cookbook examples for some advanced strategies.
#
# The key functions are:
#
# * read_sql_table(table_name, con[, schema, ...])
#     * Read SQL database table into a DataFrame.
# * read_sql_query(sql, con[, index_col, ...])
#     * Read SQL query into a DataFrame.
# * read_sql(sql, con[, index_col, ...])
#     * Read SQL query or database table into a DataFrame.
# * DataFrame.to_sql(name, con[, flavor, ...])
#     * Write records stored in a DataFrame to a SQL database.

# %%
from sqlalchemy import create_engine

# %%
engine = create_engine("sqlite:///:memory:")

# %%
pd.io.sql._is_sqlalchemy_connectable(engine)

# %%
df.to_sql("data", engine)

# %%
sql_df = pd.read_sql("data", con=engine)

# %%
sql_df
