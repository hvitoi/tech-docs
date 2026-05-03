# Lowest Common Ancestor of a Binary Tree

> [LeetCode #236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) — Medium

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor):

> "The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**)."

## Examples

### Example 1

```text
Input:  root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4],  p = 5,  q = 1
Output: 3

         3
        / \
       5   1
      / \ / \
     6  2 0  8
       / \
      7   4
```

### Example 2

```text
Input:  root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4],  p = 5,  q = 4
Output: 5
Explanation: A node can be a descendant of itself per the LCA definition.
```

### Example 3

```text
Input:  root = [1, 2],  p = 1,  q = 2
Output: 1
```

## Constraints

- The number of nodes in the tree is in the range `[2, 10^5]`.
- `-10^9 <= Node.val <= 10^9`
- All `Node.val` are unique.
- `p != q`
- `p` and `q` will exist in the tree.

## What to practise

- Recurse on both children. If left and right both return non-null, the current node is the LCA.
- If only one side returns non-null, propagate it up.
- If the current node is `p` or `q`, return it (handles "node is descendant of itself" case).
- This is the canonical *recurse-and-bubble* pattern.
