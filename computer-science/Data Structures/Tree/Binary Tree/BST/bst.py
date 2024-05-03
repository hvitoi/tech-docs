# %%
from unittest import TestCase
from collections import deque


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root: Node | None = None

    def to_set(self, node=None, acc=None):
        """Depth-First In-Order Traversal"""
        node = node if node else self.root
        acc = acc if acc is not None else set()

        if not node:
            return acc

        if node.left:
            self.to_set(node.left, acc)

        acc.add(node.data)

        if node.right:
            self.to_set(node.right, acc)

        return acc


# %%
def insert(tree: BST, value: int):
    def insert_(node: Node, value: int):
        if value == node.data:
            raise Exception("Duplicated value")

        if value < node.data:
            if node.left:
                insert_(node.left, value)
            else:
                node.left = Node(value)

        if value > node.data:
            if node.right:
                insert_(node.right, value)
            else:
                node.right = Node(value)

    if not tree.root:
        tree.root = Node(value)
        return

    insert_(tree.root, value)


bst = BST()
insert(bst, 8)
insert(bst, 10)
insert(bst, 3)
insert(bst, 1)

test_case = TestCase()
test_case.assertEqual({1, 3, 8, 10}, bst.to_set())


# %%
def lookup(tree: BST, target: int) -> bool:
    def lookup_(node: Node | None, target: int) -> bool:
        """Depth-First Pre-Order Traversal"""
        if not node:
            return False

        if target == node.data:
            return True

        if target < node.data:
            return lookup_(node.left, target)

        if target > node.data:
            return lookup_(node.right, target)

        return False

    return lookup_(tree.root, target)


test_case = TestCase()
test_case.assertEqual(True, lookup(bst, 3))
test_case.assertEqual(False, lookup(bst, 99))


# %%
def traverse_breath_first(tree: BST) -> list[int]:
    def bfs(root: Node | None) -> list[int]:
        acc = []

        if not root:
            return acc

        queue = deque([root])

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

    return bfs(tree.root)


test_case = TestCase()
test_case.assertEqual(traverse_breath_first(bst), [8, 3, 10, 1])


# %%
def traverse_depth_first(tree: BST) -> list[int]:
    def dfs(node: Node | None) -> list[int]:
        """Depth-First In-Order"""
        acc = []

        if not node:
            return acc

        acc.extend(dfs(node.left))
        acc.append(node.data)
        acc.extend(dfs(node.right))

        return acc

    return dfs(tree.root)


test_case = TestCase()
test_case.assertEqual(traverse_depth_first(bst), [1, 3, 8, 10])


# %%
def height(tree: BST):
    def height_(node: Node | None):
        if not node:
            return -1

        return max(
            1 + height_(node.left),
            1 + height_(node.right),
        )

    return height_(tree.root)


test_case.assertEqual(height(bst), 2)
