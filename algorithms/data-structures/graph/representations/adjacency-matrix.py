# A list containing each node in order. Each node itself is a list containing if it's connected (0 or 1) with each of the other nodes. It can also contain weights (scalar) and directions (sign)

# %%
# as a list
graph = [
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0],
]

# as a map
graph = {
    0: [0, 0, 1, 0],
    1: [0, 0, 1, 1],
    2: [1, 1, 0, 1],
    3: [0, 1, 1, 0],
}
