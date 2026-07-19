# %%

isinstance(9, int)

# %%
assert isinstance({}, dict)  # allows subclasses — usually what you want
assert type({}) is dict  # exact type, no subclasses
