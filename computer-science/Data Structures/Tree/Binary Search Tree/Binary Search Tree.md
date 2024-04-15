# Binary Search Tree (BST)

- A tree structure to store numbers in a sorted fashion so that searching on it is easy
- <https://visualgo.net/en/bst>

## Nodes/Levels relationship

$$h = \lfloor log_2(n) \rfloor + 1$$

Where

- $h = number\ of\ levels$
- $n = number\ of\ nodes$

## Operations

- `Lookup`: $O(log\ n)$
- `Insert`: $O(log\ n)$
- `Delete`: $O(log\ n)$

## Balancing a BST

- As new elements get added to the BST, the tree can become `unbalanced`
  - E.g., many levels, but the deeper levels have few elements
  - This happens especially when adding elements in increasing order
- An extremely unbalanced BST turns into a `Linked List` and the search becomes $O(n)$
