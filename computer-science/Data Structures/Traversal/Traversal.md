# Traversal

- **Traversal**: loop thorough all the elements in a given data structure (just because)

- `Example`: in a Linked List, the traversal stops when the next element points to null
- Traversals are usually implemented with a `while`/`for` and a defined `stop rule` according to each data structure

## Breadth-first traverse

- Visit order: by level, from left to right
- Can be implemented using a `queue` to append the element of the next layer into the end of the processing queue

- In `graphs`, it travels first the shortest paths (fewer hops) if no weights are considered
  - E.g., most related items, closest friends

- **Space complexity**
  - It needs to keep track of all the nodes in the next level
  - In a perfect binary tree it's $O(n)$
  - The last level contains half of the total items

```python
def traverse_breath_first_binary_tree(node: Node) -> list:
    acc = []

    if not node:
        return acc

    queue = deque([node])

    while queue:
        # consume first element in the queue
        node = queue.popleft()
        acc.append(node.data)

        # append its children to the end of the queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return acc
```

## Depth-first traverse

- **Pre order** traversal
  - Visit order: node, left, right
  - Good to recreate a tree. The insertion would be the same
- **In order** traversal
  - Visit order: left, node, right
  - In a BST the output is sorted
- **Post order** traversal
  - Visit order: left, right, node

- Can be implemented using a `stack` (stack data structure or the callstack/recursion) to call the nodes starting from the root node

- In `graphs`, it can be used to solve mazes
  - It will go first to the leaves and the exits are located on the borders

- **Space complexity**
  - It's the call stack heigh (or the tree height)
  - $O(log\ n)$

```python
def traverse_depth_first(tree: BST, node: Node = None):
    """Depth-First In-Order"""
    if not tree.root:
        return

    node = node if node else tree.root

    if node.left:
        traverse_depth_first(tree, node.left)

    print(node.data)

    if node.right:
        traverse_depth_first(tree, node.right)
```
