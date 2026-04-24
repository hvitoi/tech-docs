# Breadth-first search (BFS)

Explore nodes in order of distance from the source, one "level" at a time, using a FIFO queue. Guarantees shortest-path distance (in edges) in unweighted graphs.

## When to use

- Shortest path / minimum steps in an **unweighted** graph or grid.
- Level-order tree traversal (operating on all nodes at depth `d` before depth `d+1`).
- State-space search where each transition has equal cost: word ladder, puzzle solvers, minimum-moves problems.
- Bipartiteness check (two-coloring by BFS layers).

## Template

```python
from collections import deque

def bfs(start):
    q = deque([start])
    dist = {start: 0}
    while q:
        node = q.popleft()
        for nbr in graph[node]:
            if nbr not in dist:
                dist[nbr] = dist[node] + 1
                q.append(nbr)
    return dist
```

For a level-by-level pass (e.g. tree level widths), snapshot `len(q)` at the top of each outer iteration and drain that many nodes before recording the level.

## Complexity

`O(V + E)` time, `O(V)` space for the queue and visited set.

## Pitfalls

- Weighted graphs: BFS gives wrong distances — use Dijkstra or 0-1 BFS (deque, push-front for zero-weight edges).
- Mark as visited **on enqueue**, not on dequeue, or the same node gets queued multiple times.
- Grid BFS: bounds-check neighbors before pushing.
