# ---------------------------------------------------------
# Lists
amigos = ["Amilton", "Bob", "Cassio"]
coisas = ["Eu", 2, True]

print(coisas[2])                    # Get element of the list
print(amigos[1:], amigos[:2])       # Get range of elements of the list

amigos.extend(coisas)               # Amigos receives coisas
print(amigos)

amigos.append("Dario")              # Append new item to amigos
print(amigos)

amigos.insert(0, "Zerilda")           # Insert into position 0
print(amigos)

amigos.remove("Zerilda")              # Remove item
amigos.remove(True)
del(amigos[4])                         # Remove by index
print(amigos)

amigos.pop()                        # Remove last item
print(amigos)

print(amigos.index("Amilton"))      # Index of the item
print(amigos.count("Eu"))           # Appearance of the item

amigos.sort()       # Asc
print(amigos)
amigos.reverse()    # Desc
print(amigos)

print(len(amigos))

amigos2 = amigos      # Copy
print(amigos2)

amigos.clear()      # Remove everything
print(amigos)

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
