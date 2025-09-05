# %%
# https://leetcode.com/problems/validate-binary-search-tree/

import unittest


class Node:
    def __init__(self, data, *, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def is_valid_bst(node: Node, *, min=float("-inf"), max=float("inf")) -> bool:
    if (node.data < min) or (node.data > max):
        return False

    if node.left and not is_valid_bst(node.left, min=min, max=node.data):
        return False

    if node.right and not is_valid_bst(node.right, min=node.data, max=max):
        return False

    return True


test_case = unittest.TestCase()


node = Node(
    2,
    left=Node(1),
    right=Node(3),
)
test_case.assertEqual(is_valid_bst(node), True)

node = Node(
    5,
    left=Node(1),
    right=Node(
        4,
        left=Node(3),
        right=Node(6),
    ),
)
test_case.assertEqual(is_valid_bst(node), False)
