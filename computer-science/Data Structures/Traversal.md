# Traversal

- **Traversal**: loop thorough all the elements in a given data structure (just because)

- `Example`: in a Linked List, the traversal stops when the next element points to null
- Traversals are usually implemented with a `while`/`for` and a defined `stop rule` according to each data structure

## Type

- **Depth-First Search**
  - `Pre order` traversal
    - Visit order: node, left, right
  - `In order` traversal
    - Visit order: left, node, right
    - In a BST the output is sorted
  - `Post order` traversal
    - Visit order: left, right, node
  - Can be implemented using:
    - A `stack` (stack datastructure or the callstack/recursion): to call the nodes starting from the root node
- **Breadth-First Search**
  - Visit order: by level, from left to right
  - Can be implemented using:
    - A `queue`: to append the element of the next layer into the end of the processing queue

## Depth-first traverse

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

## Breadth-first traverse

```python
def traverse_breath_first(tree: BST):
    queue = [tree.root] if tree.root else []

    while queue:
        # consume first element in the queue
        node = queue.pop(0)
        print(node.data)

        # append its children to the end of the queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

## Search

- **Search** is a kind of traversal stops as soon as the target item is found

### Linear search

- Search over a `linear data structure`
  - e.g., array
- It's also called **iteration**
- Runtime complexity: $O(n)$

```python
def linear_search(arr, target):
    for el in arr:
        if el == target:
            return True
    return False
```

### Binary search

- Search in a ordered data structure, in which at each loop half of the items can discarded
  - E.g., sorted array, binary search tree
- Runtime complexity: $O(log\ n)$

```python
def binary_search(arr, target):
    if not arr:
        return False

    mid_index = len(arr) // 2

    if target == arr[mid_index]:
        return True

    if target < arr[mid_index]:
        return binary_search(arr[:mid_index], target)

    if target > arr[mid_index]:
        return binary_search(arr[mid_index + 1 :], target)
```
