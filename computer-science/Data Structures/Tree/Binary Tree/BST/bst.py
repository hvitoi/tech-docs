# %%
from unittest import TestCase
from collections import deque


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


# %%
def insert(tree: BST, data: int, node: Node = None):
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

test_case = TestCase()
test_case.assertEqual({1, 3, 8, 10}, bst.to_set())


# %%
def lookup_(node: Node, target: int) -> bool:
    """Depth-First Pre-Order Traversal"""
    if not node:
        return False

    if target == node.data:
        return True

    if target < node.data and node.left:
        return lookup_(node.left, target)

    if target > node.data and node.right:
        return lookup_(node.right, target)

    return False


def lookup(tree: BST, target: int):
    node = tree.root if tree else None
    return lookup_(node, target)


test_case = TestCase()
test_case.assertEqual(True, lookup(bst, 3))
test_case.assertEqual(False, lookup(bst, 99))


# %%
def traverse_breath_first_(node: Node) -> list[int]:
    acc = []

    if not node:
        return acc

    queue = deque([node])

    while queue:
        # consume first element in the queue
        node = queue.popleft()
        acc.append(node.data)

        # append its children to the end of the queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return acc


def traverse_breath_first(tree: BST):
    node = tree.root if tree else None
    return traverse_breath_first_(node)


test_case = TestCase()
test_case.assertEqual(traverse_breath_first(bst), [8, 3, 10, 1])


# %%
def traverse_depth_first_(node: Node, acc: list[int] = []) -> list[int]:
    """Depth-First In-Order"""

    if node.left:
        traverse_depth_first_(node.left, acc)

    acc.append(node.data)

    if node.right:
        traverse_depth_first_(node.right, acc)

    return acc


def traverse_depth_first(tree: BST):
    node = tree.root if tree else None
    return traverse_depth_first_(node)


test_case = TestCase()
test_case.assertEqual(traverse_depth_first(bst), [1, 3, 8, 10])


# %%
def is_valid_(node: Node, *, min=float("-inf"), max=float("inf")) -> bool:
    if (node.data < min) or (node.data > max):
        return False

    if node.left:
        return is_valid_(node.left, min=min, max=node.data)

    if node.right:
        return is_valid_(node.right, min=node.data, max=max)

    return True


def is_valid(tree: BST) -> bool:
    node = tree.root if tree else None
    return is_valid_(node)


test_case.assertEqual(is_valid(bst), True)


# %%
def height_(node: Node):
    if not node:
        return -1

    return max(
        1 + height_(node.left),
        1 + height_(node.right),
    )


def height(tree: BST):
    node = tree.root if tree else None
    return height_(node)


test_case.assertEqual(height(bst), 2)
