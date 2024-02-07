# %%
# lists accept multiple data types
foo = ["a", 1, True, ["c", 9]]
list("abc")  # str -> list

# %%
# Nested Lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]

for row in matrix:
    for col in row:
        print(col)

# %%
# Concatenate lists
["a", "b"] + ["c", "d"]
