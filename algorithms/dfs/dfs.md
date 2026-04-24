# Depth-first search (DFS)

Explore as far as possible along each branch before backtracking. Implemented with recursion (implicit call stack) or an explicit stack.

## When to use

- Tree traversal (preorder/inorder/postorder).
- Reachability or connected components in a graph.
- Cycle detection, topological sort (via post-order on a DAG).
- Problems where the answer depends on a full root-to-leaf or full-path exploration (paths, longest path, etc.).

## Template (graph)

```python
def dfs(node, visited):
    if node in visited: return
    visited.add(node)
    for nbr in graph[node]:
        dfs(nbr, visited)
```

For trees there is no `visited` set — each node has one parent — but you still choose the order: **preorder** (act before children), **inorder** (between left and right, BSTs), **postorder** (after children, aggregation/topo-sort).

## Complexity

`O(V + E)` time for graphs, `O(n)` for trees. Space is `O(h)` where `h` is the recursion depth (tree height, or longest simple path in a graph).

## Pitfalls

- Deep trees / long chains blow the stack — switch to an iterative stack when depth can exceed ~10⁴.
- Forgetting `visited` on graphs causes infinite loops.
- Mixing traversal orders: for BST validation use inorder; for tree serialization use pre/postorder consistently.
