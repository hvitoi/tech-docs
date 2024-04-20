# Balance

- As new elements get added to the BST, the tree can become `unbalanced` (skewed)
- An extremely unbalanced BST turns into a `Linked List` and the search becomes $O(n)$

$B(n) = H(T_L) - H(T_R)$

Where

- $B$: balance coefficient
- $H_L$: heigh of the child to the left
- $H_R$: heigh of the child to the right

## AVL tree (Adelson-Velsky and Landis)

- An **AVL Tree** is a tree is self balancing tree
- Balancing happens at each new insertion by applying rotations when necesasry
- That keeps the balance coefficient under a threshold $|B(n)| \leq 1$

## Rotations

- `Rotations` is an operation to fix an unbalanced tree
- Rotations have a $O(log\ n)$ complexity

- A **left-heavy** needs either
  - A `right rotation`
  - A `left-right rotation`
- A **right-heavy** needs either
  - A `left rotation`
  - A `right-left rotation`
