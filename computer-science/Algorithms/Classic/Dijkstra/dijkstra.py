# %%
import heapq
from unittest import TestCase


def get_path(distances, goal):
    if goal is None:
        return []
    next_path = distances[goal]["path-via"]
    return get_path(distances, next_path) + [goal]


def distance_to_a_destination(graph: dict, start: str, goal: str):
    distances = {}
    for node in graph:
        distances[node] = {}
        distances[node]["distance"] = float("inf")
        distances[node]["path-via"] = None
    distances[start]["distance"] = 0
    distances[start]["path-via"] = None

    next_nodes_to_visit = [(0, start)]
    visited_nodes = set()

    while next_nodes_to_visit:
        node_distance_from_start, node = next_nodes_to_visit.pop()

        # this if statement can be removed to get the distance to every other node
        if node == goal:
            return distances[node]["distance"], get_path(distances, node)

        for neighbor, weight in graph[node].items():
            neighbor_distance_from_start = node_distance_from_start + weight

            if neighbor_distance_from_start < distances[neighbor]["distance"]:
                distances[neighbor]["distance"] = neighbor_distance_from_start
                distances[neighbor]["path-via"] = node

            if neighbor not in visited_nodes:
                heapq.heappush(
                    next_nodes_to_visit, (neighbor_distance_from_start, neighbor)
                )

        visited_nodes.add(node)

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
    distance_to_a_destination(graph, "A", "F"),
    (10, ["A", "C", "E", "F"]),
)
