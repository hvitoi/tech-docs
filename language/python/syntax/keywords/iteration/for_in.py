# %%

# range
for i in range(10):
    print(i)

# %%

# list
for el in ["blue", "green", "red"]:
    print(el)

# %%

# string
for el in "Henrique":
    print(el)

# %%

# Tuples
for i, el in [(1, "a"), (2, "b"), (3, "c")]:
    print(i, el)

for i, el in enumerate(["a", "b", "c"]):
    print(i, el)

for k, v in {"a": 1, "b": 2}.items():
    print(k, v)

# %%

# map
my_map = {"a": "alpha", "b": "beta"}
for key in my_map:
    # iterates over the key
    print(key, my_map[key])

for key, val in my_map.items():
    print(key, val)
