# Any environment variable read from the OS is a string
# %%
import os

# Uses the C library to get the environment variable


# Get environment variable with a default fallback
os.getenv("HOME", None)
