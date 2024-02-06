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
[(x, y) for x in "abc" for y in (1, 2, 3)]
