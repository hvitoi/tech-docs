# %%
import heapq
import unittest


def build_full_path(distances, node):
    if node is None:
        return []
    next_node = distances[node]["path-via"]
    return build_full_path(distances, next_node) + [node]


def distance_to_destination(graph: dict, start_node: str, end_node: str):
    # Dictionary to store the shortest distance to the start node
    distances = {
        node: {
            "distance": float("inf"),  # shortest distance from the start
            "path-via": None,  # the last node that caused the shortest distance
        }
        for node in graph
    }
    distances[start_node]["distance"] = 0

    next_nodes_to_visit = [(0, start_node)]  # (distance_from_start, node)
    visited_nodes = set()

    while next_nodes_to_visit:
        # get the next node with the shortest distance from start
        distance_from_start, node = heapq.heappop(next_nodes_to_visit)

        # skip the node if it has already been visited

        # this if statement can be removed to get the distance to every other node
        if node == end_node:
            return distances[node]["distance"], build_full_path(distances, node)

        for neighbor, weight in graph[node].items():
            neighbor_distance_from_start = distance_from_start + weight

            if neighbor_distance_from_start < distances[neighbor]["distance"]:
                distances[neighbor]["distance"] = neighbor_distance_from_start
                distances[neighbor]["path-via"] = node

            if neighbor not in visited_nodes:
                next_node_to_visit = (neighbor_distance_from_start, neighbor)
                # A heap is used (instead of a conventional list) to optimize the process of selecting the next node with the smallest distance
                heapq.heappush(next_nodes_to_visit, next_node_to_visit)

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

test_case = unittest.TestCase()

test_case.assertEqual(
    distance_to_destination(graph, "A", "F"),
    (10, ["A", "C", "E", "F"]),
)
