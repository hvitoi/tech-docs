# %%

type("abc")  # str
type({})  # dict
type([])  # list
type(True)  # bool
type((0, "a"))  # tuple
type(None)  # NoneType

# Optional value
type(int | None)  # NoneType
