# Any environment variable read from the OS is a string
# %%
import os

# os.environ is a dict-like object with all the environment variables
print(os.environ)
os.environ.get("HOME", None)


# os.environ is mutable! You can modify envs with it
os.environ["MY_VAR"] = "new_value"
