# %%
import operator

mydict = {"foo": "bar"}

foo_getter = operator.itemgetter("foo")

foo_getter(mydict)
