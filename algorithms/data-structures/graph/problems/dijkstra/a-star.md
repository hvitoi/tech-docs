# A*

- Adds an `heuristic` on top of dijkstra algorithm
  - The heuristic is to add a `sense of correctness` on each neighbor
  - This way, we can visit only the nodes that have a right probability to be the right path
- The heuristic can be
  - "the smell of the cheese on the end of the maze" (stronger is better)
  - "the euclidean distance towards the destination node" (smaller is better)
- The heuristic is added to the actual distance (weight) at each node in order to define which is the next node to be evaluated
