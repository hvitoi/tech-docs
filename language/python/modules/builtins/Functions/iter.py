# Iterator is an object that contains a countable number of values
# Iterator is an object that can be iterated upon (a stream of elements)

# While the iterator is not yet exhausted, "next" returns the next element on the stream
# When the iterator is exhausted, "next" raises the StopIteration exception
# Iterator only take next element, never previous. You can, however, create a new iter

# Python expects iterable objects in several context, the most notable is on for loops

# %%

# tuple
it = iter(("a", "b", "c"))
next(it)

# %%

# str
it = iter("abc")
next(it)

# dict
it = iter({"a": 1, "b": 2, "c": 3})
next(it)

# %%

# iters can be materialized back into lists, tuple, dict, etc
it = iter(["a", "b", "c"])
my_list = list(it)
a, b, c = my_list
