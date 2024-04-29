# Dijkstra Algorithms

- Find the `best path` from one node to every other node
- It's a brute force solution (applies no heuristic)
- It uses a `greedy algorithm` approach that makes the local optimal choice at each node
- It uses a `priority queue` (min heap) to decide which node to visit next

## Steps

1. Create a map with the distances to every other node starting with infinity for each
1. Take the origin node and find the distances to the closest adjacent nodes (one level up - BFS)
1. Take every adjacent node (starting with the closer to the origin node - use a heap to take them in the correct order) and find every other distance to their neighbors (it must be summed with the min distance to this node from the distances map)

Throughout the flow, a set of visited nodes must be keep to avoid revisiting one node

## Complexity

$$O(E * log(V))$$
Where:

- $V$ is the number of vertices
- $E$ is the total number of edges
