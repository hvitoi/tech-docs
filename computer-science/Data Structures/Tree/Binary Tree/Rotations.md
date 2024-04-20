# Rotation

- `Rotations` is an operation to fix an unbalanced tree

## Balance

- As new elements get added to the BST, the tree can become `unbalanced` (skewed)
- An extremely unbalanced BST turns into a `Linked List` and the search becomes $O(n)$

$B(n) = H(T_L) - H(T_R)$

Where

- $B$: balance coefficient
- $H_L$: heigh of the child to the left
- $H_R$: heigh of the child to the right

An **AVL Tree** is a tree that keeps the balance coefficient under a threshold $|B(n)| \leq 1$

### Applying Rotations

- Rotation needs to be apply whenever a new item is inserted
  - The rotation happens only when a new level is added and there is still place on the previous level
  - The rotation happens only around the item that was inserted
