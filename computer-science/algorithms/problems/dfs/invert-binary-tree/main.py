# %%
# https://leetcode.com/problems/invert-binary-tree/

import unittest
import collections


class Node:
    def __init__(self, data, *, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def serialize(self) -> list:
        """
        Serializes the BST so that the BST structured is represented as a list
        It's used only for testing purposes
        """
        acc = []

        nodes = collections.deque([self])
        while nodes:
            node = nodes.popleft()

            if not node:
                acc.append(None)
                continue

            acc.append(node.data)
            nodes.append(node.left)
            nodes.append(node.right)

        while acc[-1] is None:
            acc.pop()

        return acc


def invert_binary_tree(node: Node) -> Node:
    if not node:
        return

    node.left, node.right = (
        invert_binary_tree(node.right),
        invert_binary_tree(node.left),
    )

    return node


test_case = unittest.TestCase()

tree_node = Node(
    2,
    left=Node(1),
    right=Node(3),
)
test_case.assertEqual(
    invert_binary_tree(tree_node).serialize(),
    [2, 3, 1],
)

tree_node = Node(
    5,
    left=Node(1),
    right=Node(4, left=Node(3), right=Node(6)),
)
test_case.assertEqual(
    invert_binary_tree(tree_node).serialize(),
    [5, 4, 1, 6, 3],
)
