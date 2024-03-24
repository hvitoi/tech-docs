# %%
colors = ["blue", "green", "red"]

# the enumerated object is a list of tuples [(0, v0), (1, v1), (2, v2)]
enumerated_colors = enumerate(colors)

for index, color in enumerated_colors:
    print(index, color)

# %%
# list of tuples do not need to be enumerated
tuples = [(1, "a"), (2, "b"), (3, "c")]

for index, el in tuples:
    print(index, el)
