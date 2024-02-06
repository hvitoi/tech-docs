foo = dict({"a": 1})
foo = {
    "a": 1,
    "b": 2,
    "c": 3,
}

# access elements by index
foo["a"]  # 1
foo["z"]  # exception!

# dict from iter tuple
items = [("a", 1), ("b", 2), ("c", 3)]
myit = iter(items)
dict(myit)
