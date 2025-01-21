# %%
colors = ["red", "green", "blue"]

# the enumerated object is a list of tuples [(0, "red"), (1, "green"), (2, "blue")]
enumerated_colors = enumerate(colors)

for index, color in enumerated_colors:
    print(index, color)

# %%
# list of tuples do not need to be enumerated
tuples = [(1, "a"), (2, "b"), (3, "c")]

for index, el in tuples:
    print(index, el)

# %%
# Remove multiple indexes from an array
# It's useful because using a traditional for would shift indexes during the execution
arr = ["a", "b", "c", "d", "e"]
[item for i, item in enumerate(arr) if i not in {1, 2}]
