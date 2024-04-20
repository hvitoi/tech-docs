# %%
from unittest import TestCase

type Vertex = int
type VertexEdges = set(Vertex)
type Graph = dict(Vertex, VertexEdges)  # Adjacent List


test_case = TestCase()


# %%
def add_vertex(graph: Graph, vertex: Vertex):
    graph[vertex] = set()


graph = dict()
add_vertex(graph, 0)
add_vertex(graph, 1)
add_vertex(graph, 2)
add_vertex(graph, 3)

test_case.assertEqual(
    graph,
    {
        0: set(),
        1: set(),
        2: set(),
        3: set(),
    },
)


# %%
def add_edge(graph: Graph, vertex1: Vertex, vertex2: Vertex):
    graph[vertex1].add(vertex2)
    graph[vertex2].add(vertex1)


graph = dict()
add_vertex(graph, 0)
add_vertex(graph, 1)
add_vertex(graph, 2)
add_vertex(graph, 3)

add_edge(graph, 3, 1)
add_edge(graph, 1, 2)
add_edge(graph, 1, 0)
add_edge(graph, 0, 2)

test_case.assertEqual(
    graph,
    {
        0: {1, 2},
        1: {0, 2, 3},
        2: {0, 1},
        3: {1},
    },
)
