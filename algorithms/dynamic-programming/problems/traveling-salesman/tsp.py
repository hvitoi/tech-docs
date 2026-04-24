# %%
import unittest


def tsp_nearest_neighbor(graph: dict[str, dict[str, int]], start: str):
    visited_nodes = set()
    path = []
    total_distance = 0

    current_node = start

    while len(visited_nodes) != len(graph):
        path.append(current_node)
        visited_nodes.add(current_node)

        next_node = (None, float("inf"))
        for node, distance in graph[current_node].items():
            if node not in visited_nodes and distance < next_node[1]:
                next_node = (node, distance)

        total_distance += next_node[1] if next_node[0] else 0
        current_node = next_node[0]

    # close the circuit
    total_distance += graph[path[-1]][start]
    path.append(start)

    return path, total_distance


test_case = unittest.TestCase()

graph = {
    "A": {"A": 0, "B": 10, "C": 15, "D": 20},
    "B": {"A": 10, "B": 0, "C": 35, "D": 25},
    "C": {"A": 15, "B": 35, "C": 0, "D": 30},
    "D": {"A": 20, "B": 25, "C": 30, "D": 0},
}
# 10 + 25 + 30
test_case.assertEqual(
    tsp_nearest_neighbor(graph, "A"),
    (["A", "B", "D", "C", "A"], 80),
)
