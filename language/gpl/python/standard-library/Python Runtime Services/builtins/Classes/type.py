# %%

type("abc")  # str
type({})  # dict
type([])  # list
type(True)  # bool
type((0, "a"))  # tuple
type(None)  # NoneType

# Optional value
type(int | None)  # NoneType

# %%
assert isinstance({}, dict)  # allows subclasses — usually what you want
assert type({}) is dict  # exact type, no subclasses
