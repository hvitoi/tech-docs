# %%
import pprint


foo = {"a": 1, "b": {"c": 2, "d": 3}}

# does not indent the output
pp = pprint.PrettyPrinter()
pp.pprint(foo)
