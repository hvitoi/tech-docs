# %%

# GENEXPS
# Concept borrowed from Haskell
# Returns an iterator
# Syntax: expression for item in iterable if condition == True

my_generator = (el for el in range(10))  # the pure form of the generator
my_list = [el for el in range(10)]
my_int = sum(el for el in range(10))

type(my_generator)  # generator
type(my_list)  # list
type(my_int)  # int
