foo = {
    "a": 1,
    "b": 2,
    "c": 3,
}

foo.get("a")
foo.get("z")  # returns nothing
foo.get("z", "Not a valid key")  # returns the default value
