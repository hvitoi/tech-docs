# %%
import heapq
from unittest import TestCase


def distances_map(graph: dict, origin: str):
    distances = dict.fromkeys(graph.keys(), float("inf"))
    distances[origin] = 0

    next_nodes = [(0, origin)]
    seen_nodes = set()

    while next_nodes:
        _, current_node = next_nodes.pop()
        neighbors = graph[current_node]

        for neighbor in neighbors:
            distance_from_origin = distances[current_node] + neighbors[neighbor]

            if distance_from_origin < distances[neighbor]:
                distances[neighbor] = distance_from_origin

            if neighbor not in seen_nodes:
                heapq.heappush(next_nodes, (distance_from_origin, neighbor))

        seen_nodes.add(current_node)

    return distances


def distances_map_with_paths(graph: dict, origin: str):
    distances = {}
    for node in graph:
        distances[node] = {}
        distances[node]["distance"] = float("inf")
        distances[node]["prev"] = None

    distances[origin] = {"distance": 0}

    next_nodes = [(0, origin)]
    seen_nodes = set()

    while next_nodes:
        _, current_node = next_nodes.pop()
        neighbors = graph[current_node]

        for neighbor in neighbors:
            distance_from_origin = (
                distances[current_node]["distance"] + neighbors[neighbor]
            )

            if distance_from_origin < distances[neighbor]["distance"]:
                distances[neighbor]["distance"] = distance_from_origin
                distances[neighbor]["prev"] = current_node

            if neighbor not in seen_nodes:
                heapq.heappush(next_nodes, (distance_from_origin, neighbor))

        seen_nodes.add(current_node)

    return distances


graph = {
    "A": {"B": 2, "C": 4},
    "B": {"A": 2, "C": 3, "D": 8},
    "C": {"A": 4, "B": 3, "D": 2, "E": 5},
    "D": {"B": 8, "C": 2, "E": 11, "F": 22},
    "E": {"C": 5, "D": 11, "F": 1},
    "F": {"D": 22, "E": 1},
}

test_case = TestCase()

test_case.assertEqual(
    distances_map(graph, "A"),
    {"A": 0, "B": 2, "C": 4, "D": 6, "E": 9, "F": 10},
)


test_case.assertEqual(
    distances_map_with_paths(graph, "A"),
    {
        "A": {"distance": 0},
        "B": {"distance": 2, "prev": "A"},
        "C": {"distance": 4, "prev": "A"},
        "D": {"distance": 6, "prev": "C"},
        "E": {"distance": 9, "prev": "C"},
        "F": {"distance": 10, "prev": "E"},
    },
)
