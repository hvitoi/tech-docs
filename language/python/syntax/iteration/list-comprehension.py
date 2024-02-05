# LISTCOMP
# Concept borrowed from Haskell
# Returns a list

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
foo = [1, 2, 3, 4]

# pick the element times itself, for each element in foo
[el**2 for el in foo]

# pick the element, for each element in foo, if the element is divisible by 2
[el for el in foo if el % 2 == 0]

# new list from a range
[x for x in range(10)]

# syntax
# newlist = [expression for item in iterable if condition == True]

# List comprehension itself returns an iterable object, that's why it can be directly put into a list using the syntax [myiter]
# Generator expression can be used to return a pure generator instead


seq1 = "abc"
seq2 = (1, 2, 3)
[(x, y) for x in seq1 for y in seq2]
# [('a', 1), ('a', 2), ('a', 3),
#  ('b', 1), ('b', 2), ('b', 3),
#  ('c', 1), ('c', 2), ('c', 3)]
