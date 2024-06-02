# %%
import json


foo = {"a": 1, "b": {"c": 2, "d": 3}}
indented_foo = json.dumps(foo, indent=4)
print(indented_foo)
