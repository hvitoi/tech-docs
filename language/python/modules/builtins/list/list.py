# lists accept multiple data types
foo = ["a", 1, True, ["c", 9]]


# accessing elements
foo[2]  # get value from index 2
foo[3][1]  # nested element
foo[1:]  # from index 1 on
foo[:2]  # until index 2 (not inclusive)
foo[1:2]

# write elements
foo[0] = "lala"  # index 0 is replaced

# Nested Lists
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:
    for col in row:
        print(col)


# remove element by index
del (foo[2])

# length
len(foo)
