# A list containing each node in order. Each node itself is a list containing all its connections (with other nodes)

# %%
# as a list
graph = [
    ["C"],
    ["C", "D"],
    ["A", "B", "D"],
    ["B", "C"],
]

# as a map
graph = {
    "A": ["C"],
    "B": ["C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"],
}

# as a map (weighted)
graph = {
    "A": {"C": 2},
    "B": {"C": 2, "D": 4},
    "C": {"A": 1, "B": 1, "D": 2},
    "D": {"B": 7, "C": 5},
}
