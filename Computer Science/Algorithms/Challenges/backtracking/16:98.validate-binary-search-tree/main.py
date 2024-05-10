# %%

from unittest import TestCase


class TreeNode:
    def __init__(self, val, *, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(node: TreeNode, *, min=float("-inf"), max=float("inf")) -> bool:
    if (node.val < min) or (node.val > max):
        return False

    if node.left and not is_valid_bst(node.left, min=min, max=node.val):
        return False

    if node.right and not is_valid_bst(node.right, min=node.val, max=max):
        return False

    return True


test_case = TestCase()


node = TreeNode(
    2,
    left=TreeNode(1),
    right=TreeNode(3),
)
test_case.assertEqual(is_valid_bst(node), True)

node = TreeNode(
    5,
    left=TreeNode(1),
    right=TreeNode(
        4,
        left=TreeNode(3),
        right=TreeNode(6),
    ),
)
test_case.assertEqual(is_valid_bst(node), False)
