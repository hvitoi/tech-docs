
# iterator is an object that contains a countable number of values
# iterator is an object that can be iterated upon (a stream of elements)
# while the iterator is not yet exhausted, "next" returns the next element in the stream
# when the iterator is exhausted, "next" raises the StopIteration exception
# iterator only take next element, never previous. You can, however, create a new iter

# python expects iterable objects in several context, the most notable is on for loops
# "for X in Y", Y must be an iterable object (that can be called with iter)

# Tuple
myit = iter(("a", "b", "c"))  # start the iterator
next(myit)

# String
myit = iter("abc")
next(myit)

# Dictionary
mydict = {"a": 1, "b": 2, "c": 3}
next(iter(mydict))  # iterates over the keys
next(items(iter(mydict)))  # trick to iterate over items (key + value)

# iters can be materialized back into lists, tuple, dict, etc
myit = iter(["a", "b", "c"])
mylist = list(myit)
a, b, c = myit  # a="a" b="b" c="c"
