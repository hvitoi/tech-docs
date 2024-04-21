# %%

from unittest import TestCase


class TreeNode:
    def __init__(self, val, *, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def to_list(self, node=None, acc=None) -> list:
        """Depth-First Pre-Order"""
        node = node if node else self
        acc = acc if acc is not None else []

        if not node:
            return acc

        acc.append(node.val)

        if node.left:
            self.to_list(node.left, acc)

        if node.right:
            self.to_list(node.right, acc)

        return acc


def invert_binary_tree(root: TreeNode) -> TreeNode:
    if not root:
        return

    root.left, root.right = (
        invert_binary_tree(root.right),
        invert_binary_tree(root.left),
    )

    return root


test_case = TestCase()

node = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
test_case.assertEqual(invert_binary_tree(node).to_list(), [2, 3, 1])

node = TreeNode(
    5, left=TreeNode(1), right=TreeNode(4, left=TreeNode(3), right=TreeNode(6))
)
test_case.assertEqual(invert_binary_tree(node).to_list(), [5, 4, 6, 3, 1])
