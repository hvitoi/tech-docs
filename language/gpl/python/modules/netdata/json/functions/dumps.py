# %%
# Serialize to json
import json

data = {"a": 1, "b": {"c": 2, "d": 3}}
indented_json = json.dumps(data, indent=4)
print(indented_json)
