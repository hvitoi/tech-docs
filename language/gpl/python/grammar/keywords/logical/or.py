# %%
if (1 == 2) or (1 == 3) or (1 == 1):
    print("Matches!")


# %%
if None or "None":
    print("Matches!")

# %%
if None or True:
    print("Matches!")

# %%
foo = None or "1"
foo  # 1
