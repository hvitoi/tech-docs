# %%
from typing import Any
from unittest import TestCase


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def to_set(self, elements=set(), node=None):
        """Depth-First In-Order Traversal"""
        if self.root is None:
            return set()

        node = node if node is not None else self.root

        if node.left:
            elements = self.to_set(elements, node.left)

        elements.add(node.data)

        if node.right:
            elements = self.to_set(elements, node.right)

        return elements


test_case = TestCase()


# %%
def insert(tree: BST, data: Any, node: Node = None) -> None:
    new_node = Node(data)

    if tree.root is None:
        tree.root = new_node
        return

    node = node if node is not None else tree.root

    if data == node.data:
        raise Exception("Duplicated value")

    if data < node.data:
        if node.left is None:
            node.left = new_node
        else:
            insert(tree, data, node.left)

    if data > node.data:
        if node.right is None:
            node.right = new_node
        else:
            insert(tree, data, node.right)


bst = BST()
insert(bst, 8)
insert(bst, 10)
insert(bst, 3)
insert(bst, 1)

test_case.assertEqual({1, 3, 8, 10}, bst.to_set())


# %%
def lookup(tree: BST, target, node=None) -> bool:
    node = node if node is not None else tree.root

    if node is None:
        return False

    if target == node.data:
        return True

    if target > node.data and isinstance(node.right, Node):
        return lookup(tree, target, node.right)

    if target < node.data and isinstance(node.left, Node):
        return lookup(tree, target, node.left)

    return False


test_case.assertEqual(True, lookup(bst, 3))
test_case.assertEqual(False, lookup(bst, 99))
