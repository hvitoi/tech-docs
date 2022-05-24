foo = ["a", 1, True]

foo[2]                    # Get element of the list
foo[1:]
foo[:2]       # Get range of elements of the list

foo.extend(coisas)               # foo receives coisas


foo.append("Dario")              # Append new item to foo

foo.insert(0, "Zerilda")           # Insert into position 0


foo.remove("Zerilda")              # Remove item
foo.remove(True)
del(foo[4])                         # Remove by index


foo.pop()                        # Remove last item


foo.index("Amilton")      # Index of the item
foo.count("Eu")           # Appearance of the item

foo.sort()       # Asc

foo.reverse()    # Desc


len(foo)

foo2 = foo      # Copy


foo.clear()      # Remove everything

# -----------------------------------
# 2D List
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:
    for col in row:
        print(col)
