# Tree

- A trees is a `acyclic connected graph`
  - acyclic: no cycles
  - connected: all elements are reached from each other (no disjoint segments)
- `Parent-Child` data structure
- A filesystem directory structure is a tree starting from `/` (root node)
  - Where a folder is the parent and the files are the children

## Elements of a tree

- **Root**: node with no parent (there is only one in the tree)
- **Parent**: upstream node of a child node
- **Child**: downstream node of a parent node
- **Leaf**: nodes with no children
- **Sibling**: nodes in the same level in the tree

## Traversal

- DFS variants
  - **Pre-order**: `node -> left -> right` (Usually the most common traversal for n-ary-trees)
  - **In-order**: `left -> node -> right` (Especially useful for BST, to yield in ascending order)
  - **Post-order**: `left -> right -> node`

- BFS variants
  - **Level-order**: level by level, left to right
