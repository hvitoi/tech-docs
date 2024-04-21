# %%

from unittest import TestCase


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val, node=None):
        node = node if node else self
        if val < node.val:
            if node.left:
                self.insert(val, node.left)
            else:
                node.left = TreeNode(val)
        if val > node.val:
            if node.right:
                self.insert(val, node.right)
            else:
                node.right = TreeNode(val)

    def to_list_post_order(self, node=None, acc=None):
        node = node if node else self
        acc = acc if acc is not None else []

        if not node:
            return acc

        acc.append(node.val)

        if node.left:
            self.to_list_post_order(node.left, acc)

        if node.right:
            self.to_list_post_order(node.right, acc)

        return acc


def invert_binary_tree(root: TreeNode) -> TreeNode:
    if not root:
        return

    root.left, root.right = root.right, root.left
    return root


node = TreeNode(2)
node.insert(1)
node.insert(3)

test_case = TestCase()

test_case.assertEqual(node.to_list_post_order(), [2, 1, 3])

test_case.assertEqual(invert_binary_tree(node).to_list_post_order(), [2, 3, 1])
