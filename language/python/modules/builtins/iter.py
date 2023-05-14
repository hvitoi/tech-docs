
# iterator is an object that contains a countable number of values
# iterator is an object that can be iterated upon
# when the iterator is exhausted, it retuns a StopIteration

# Tuple
myit = iter(("a", "b", "c"))  # start the iterator
next(myit)

# String
myit = iter("abc")
next(myit)

# Dictionary
myit = iter({"a": 1, "b": 2, "c": 3})
next(myit)  # iterates over the index
