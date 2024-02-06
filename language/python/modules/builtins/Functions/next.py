# %%
it = iter(("a", "b", "c", "d", "e"))
next(it)
it.__next__()  # same
next(it)
next(it)
next(it)
next(it)  # raises StopIteration
