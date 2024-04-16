# Binary Tree

- A special kind of tree with a few rules
  - Each node can have `at most 2 child nodes`
  - Each node must have only one parent

## Node & Tree

```python
class Node:
    def __init__(self, data, *, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None
```

## Variations

- **Binary Tree**
  - Each node has up to 2 children
- **Full Binary Tree**
  - It's a BT
  - Plus each node has either 0 or 2 children
- **Complete Binary Tree**
  - It's a BT
  - Plus it's filled from top to bottom, left to right
- **Perfect Binary Tree**
  - It's a BT
  - Plus the last level is completely filled
  - Properties
    1. Number of total nodes doubles at each level: 1, 2, 4, 8, ...
    1. Number of nodes on the last level is equal to the numbers of nodes on all the other level plus one (half of the data is the bottom level)

## Traversal

- **Depth-First Search**
  - `Pre order` traversal
    - Visit order: node, left, right
  - `In order` traversal
    - Visit order: left, node, right
    - In a BST the output is sorted
  - `Post order` traversal
    - Visit order: left, right, node
  - Can be implemented using:
    - A `stack (callstack)`: to recursively call the nodes starting from the root node
- **Breadth-First Search**
  - Visit order: by level, from left to right
  - Can be implemented using:
    - A `queue`: to append the element of the next layer into the end of the processing queue
