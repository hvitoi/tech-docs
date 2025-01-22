# %%
#  https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

import unittest
import collections


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def serialize(root: Node) -> list:
    """
    Serializes the BST so that the BST structured is represented as a list
    It's used only for testing purposes
    """
    acc = []

    nodes = collections.deque([root]) if root else collections.deque()
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


def insert(node: Node, num: list):
    """
    Insert 'num' into a 'node' in a BST
    """
    if num <= node.data:
        if node.left:
            insert(node.left, num)
        else:
            node.left = Node(num)

    if num > node.data:
        if node.right:
            insert(node.right, num)
        else:
            node.right = Node(num)


def create_skewed_bst(nums: list) -> Node | None:
    """
    Insert elements to the BST in the order they are in the list
    This order of insertion may create an extremely skewed tree (a linked list)
    """

    if not nums:
        return

    root = Node(nums[0])

    for num in nums[1:]:
        insert(root, num)

    return root


def create_balanced_bst(nums: list, root=None) -> Node | None:
    """
    Insert elements to the BST in an optimal order so that the tree has the minimum height possible
    """

    if not nums:
        return

    mid_index = len(nums) // 2

    if root:
        insert(root, nums[mid_index])
    else:
        root = Node(nums[mid_index])

    create_balanced_bst(nums[:mid_index], root)
    create_balanced_bst(nums[mid_index + 1 :], root)

    return root


test_case = unittest.TestCase()

test_case.assertEqual(
    serialize(create_skewed_bst([1, 2, 3, 4, 5, 6, 7])),
    [1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7],
)

test_case.assertEqual(
    serialize(create_balanced_bst([1, 2, 3, 4, 5, 6, 7])),
    [4, 2, 6, 1, 3, 5, 7],
)

test_case.assertEqual(
    serialize(create_balanced_bst([-10, -3, 0, 5, 9])),
    [0, -3, 9, -10, None, 5],
)


test_case.assertEqual(
    serialize(create_balanced_bst([1, 3])),
    [3, 1],
)
