foo = dict({"a": 1})
foo = {
    "a": 1,
    "b": 2,
    "c": 3,
}

# access elements by index
foo["a"]  # 1
foo["z"]  # exception!

foo.get("a")
foo.get("z")  # returns nothing
foo.get("z", "Not a valid key")  # returns the default value
