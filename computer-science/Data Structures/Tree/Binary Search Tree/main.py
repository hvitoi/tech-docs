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
        if not self.root:
            return set()

        node = node if node else self.root

        if node.left:
            elements = self.to_set(elements, node.left)

        elements.add(node.data)

        if node.right:
            elements = self.to_set(elements, node.right)

        return elements


test_case = TestCase()


# %%
def insert(tree: BST, data: Any, node: Node = None):
    new_node = Node(data)

    if not tree.root:
        tree.root = new_node
        return

    node = node if node else tree.root

    if data == node.data:
        raise Exception("Duplicated value")

    if data < node.data:
        if node.left:
            insert(tree, data, node.left)
        else:
            node.left = new_node

    if data > node.data:
        if node.right:
            insert(tree, data, node.right)
        else:
            node.right = new_node


bst = BST()
insert(bst, 8)
insert(bst, 10)
insert(bst, 3)
insert(bst, 1)

test_case.assertEqual({1, 3, 8, 10}, bst.to_set())


# %%
def lookup(tree: BST, target, node=None) -> bool:
    """Depth-First Pre-Order Traversal"""
    if not tree.root:
        return False

    node = node if node else tree.root

    if target == node.data:
        return True

    if target < node.data and node.left:
        return lookup(tree, target, node.left)

    if target > node.data and node.right:
        return lookup(tree, target, node.right)

    return False


test_case.assertEqual(True, lookup(bst, 3))
test_case.assertEqual(False, lookup(bst, 99))


# %%
def traverse_breath_first(tree: BST):
    queue = [tree.root] if tree.root else []

    while queue:
        # consume first element in the queue
        node = queue.pop(0)
        print(node.data)

        # append its children to the end of the queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


traverse_breath_first(bst)


# %%
def traverse_depth_first(tree: BST, node: Node = None):
    """Depth-First In-Order"""
    if not tree.root:
        return

    node = node if node else tree.root

    if node.left:
        traverse_depth_first(tree, node.left)

    print(node.data)

    if node.right:
        traverse_depth_first(tree, node.right)


traverse_depth_first(bst)
