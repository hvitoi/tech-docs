# %%
import os
# Any environment variable read from the OS is a string


# Get environment variable with a default fallback
os.getenv("HOME", None)  # same as os.environ.get
