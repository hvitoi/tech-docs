# %%

# Range
for i in range(10):
    print(i)

# %%

# Lists
for el in ["blue", "green", "red"]:
    print(el)

# %%

# Strings
for el in "Henrique":
    print(el)

# %%

# Tuples
for i, el in [(0, "a"), (1, "b"), (2, "c")]:
    print(i, el)

for i, el in enumerate(["a", "b", "c"]):
    print(i, el)

for k, v in {0: "a", 1: "b", 2: "c"}.items():
    print(k, v)

# %%

# Maps

my_map = {"a": "alpha", "b": "beta"}
for key in my_map:
    # iterates over the key only
    print(key, my_map[key])

for key, val in my_map.items():
    print(key, val)
