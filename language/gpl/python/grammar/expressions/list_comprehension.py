# %%
# LISTCOMP
# Concept borrowed from Haskell
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# List comprehension is a generator that is forced into a list [my_generator]

[el for el in range(10)]  # same as list(range(10))
[el**2 for el in range(10)]
foo = [el for el in range(10) if el % 2 == 0]


# %%
# Nested fors
[
    item
    for row in [
        ["a", "b", "c"],
        ["d", "e", "f"],
    ]
    for item in row
]

# %%
# Remove multiple indexes from an array
# It's useful because using a traditional for would shift indexes during the execution
arr = ["a", "b", "c", "d", "e"]
[item for i, item in enumerate(arr) if i not in {1, 2}]
