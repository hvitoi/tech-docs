# GENEXPS
# Concept borrowed from Haskell
# Returns an iterator

# Generator Expressions are preferable for a pipeline of processing a stream of data

line_list = ['  line 1\n', 'line 2  \n', ' \n', '']

# Generator expression -- returns iterator
stripped_iter = (line.strip() for line in line_list)

# List comprehension -- returns list
stripped_list = [line.strip() for line in line_list]

# generators can be passed directly to functions
sum(len(el) for el in ["Henri", "que"])
