# Binary Tree

- A special kind of tree with a few rules
  - Each node can have `at most 2 child nodes`
  - Each node must have only one parent

## Node

```python
class Node:
    def __init__(self, data, *, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
```

## Variations

- **Binary Tree**: each node has up to 2 children
- **Full Binary Tree**: each node has either 0 or 2 children
- **Perfect Binary Tree**: each node has exactly 2 children
  1. Number of total nodes doubles at each level: 1, 2, 4, 8, ...
  1. Number of nodes on the last level is equal to the numbers of nodes on all the other level plus one (half of the data is the bottom level)
