# %%
my_list = ["a", "b", "c"]
enumerated_list = enumerate(my_list)  # [(0, "a"), (1, "b"), (2, "c")]

for i, el in enumerated_list:
    print(i, el)

# %%
# list of tuples do not need to be enumerated
tuples = [(1, "a"), (2, "b"), (3, "c")]

for i, el in tuples:
    print(i, el)

# %%
# Remove multiple indexes from an array
# It's useful because using a traditional for would shift indexes during the execution
arr = ["a", "b", "c", "d", "e"]
[item for i, item in enumerate(arr) if i not in {1, 2}]
