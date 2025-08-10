# %%
foo = ["a", "b", "c", "d", "e"]
foo[0]  # first
foo[-1]  # last
foo[-2]  # second last

# %%
foo = ["a", "b", "c", "d", "e"]
foo[99]  # Throws!

# %%
foo = []
foo[-1]  # Throws! (tries to get index 0)
