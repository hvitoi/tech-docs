# %%
raise Exception("An error has been found")

# %%
try:
    value = 10 / 0
except Exception as err:
    print("An exception occurred:", err)
    raise  # re-raise the same exception
