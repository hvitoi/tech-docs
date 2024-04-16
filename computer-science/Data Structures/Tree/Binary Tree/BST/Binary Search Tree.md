
# Binary Search Tree (BST)

- A tree structure to store numbers in a sorted fashion so that searching on it is easy
- <https://visualgo.net/en/bst>

## Balancing a BST

- As new elements get added to the BST, the tree can become `unbalanced`
- An extremely unbalanced BST turns into a `Linked List` and the search becomes $O(n)$

- **AVL Tree**
  - The tree is automatically rebalanced on new item insertions
  - The rebalance happens only when a new level is added and there is still place on the previous level
  - The rebalance happens only around the item that was inserted
- **Red Black Tree**
  - Also self balancing

## Operations

- `Lookup`: $O(log\ n)$
- `Insert`: $O(log\ n)$
- `Delete`: $O(log\ n)$
