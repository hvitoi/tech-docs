# Binary Tree

- A special kind of tree with a few rules
  - Each node can have `up to 2 child nodes`
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

- **Full Binary Tree**
  - Each node has either 0 or 2 children
- **Complete Binary Tree**
  - It has a filling order: top to bottom, left to right
- **Perfect Binary Tree**
  - The last level is completely filled

## Tree properties

> Strictly applies only to perfect binary trees, but can be generalized for any kind of binary tree

$$h(n) = \lfloor log_2(n) \rfloor + 1$$
$$h(n) = 1 + h(n-1)$$
Where

- $h = number\ of\ levels$
- $n = number\ of\ nodes$

That means

- The number of total nodes doubles at each level: 1, 2, 4, 8, ...
- The number of nodes on the last level is equal to the numbers of nodes on all the other level plus one (half of the data is the bottom level)

> Heigh is -1 if there is no Nodes
