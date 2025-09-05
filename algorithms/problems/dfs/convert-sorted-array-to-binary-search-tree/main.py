# %%
#  https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

import unittest
import collections


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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


def create_balanced_bst(nums: list) -> Node | None:
    """
    Insert elements to the BST in an optimal order so that the tree has the minimum height possible
    """

    if not nums:
        return

    mid_index = len(nums) // 2

    node = Node(nums[mid_index])
    node.left = create_balanced_bst(nums[:mid_index])
    node.right = create_balanced_bst(nums[mid_index + 1 :])

    return node


test_case = unittest.TestCase()


bst = create_balanced_bst([1, 2, 3, 4, 5, 6, 7])
test_case.assertEqual(
    bst.serialize(),
    [4, 2, 6, 1, 3, 5, 7],
)

bst = create_balanced_bst([-10, -3, 0, 5, 9])
test_case.assertEqual(
    bst.serialize(),
    [0, -3, 9, -10, None, 5],
)


bst = create_balanced_bst([1, 3])
test_case.assertEqual(
    bst.serialize(),
    [3, 1],
)
