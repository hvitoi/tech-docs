# %%
from os import environ

# Any environment variable read from the OS is a string


# Get environment variable with a default fallback
environ.get("HOME", None)
