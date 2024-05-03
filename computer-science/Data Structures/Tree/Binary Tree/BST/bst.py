# %%
from unittest import TestCase
from collections import deque


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BST:
    def __init__(self, elements: list | None = None):
        self.root: Node | None = None

        if elements:
            for el in elements:
                self.insert(el)

    def insert(self, value: int) -> None:
        """
        Insert an element to the BST
        """

        def insert_(node: Node, value: int) -> None:
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

        if not self.root:
            self.root = Node(value)
            return

        insert_(self.root, value)

    def search(self, target: int) -> bool:
        """
        Returns whether an element is found in the tree
        """

        def search_(node: Node | None, target: int) -> bool:
            """Depth-First Pre-Order Traversal"""
            if not node:
                return False

            if target == node.data:
                return True

            if target < node.data:
                return search_(node.left, target)

            if target > node.data:
                return search_(node.right, target)

            return False

        return search_(self.root, target)

    def to_set(self, node=None, acc=None):
        """
        Traverse Depth First and add elements to a list
        Depth-First Pre-Order Traversal
        """

        node = node if node else self.root
        acc = acc if acc is not None else set()

        if not node:
            return acc

        acc.add(node.data)

        if node.left:
            self.to_set(node.left, acc)

        if node.right:
            self.to_set(node.right, acc)

        return acc

    def to_list_df(self) -> list[int]:
        """
        Traverse Depth-First and add elements to a list
        """

        def dfs(node: Node | None) -> list[int]:
            """Depth-First In-Order"""
            acc = []

            if not node:
                return acc

            acc.extend(dfs(node.left))
            acc.append(node.data)
            acc.extend(dfs(node.right))

            return acc

        return dfs(self.root)

    def to_list_bf(self) -> list[int]:
        """
        Traverse Breadth-First and add elements to a list
        """

        def bfs(node: Node | None) -> list[int]:
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

        return bfs(self.root)

    def height(self) -> int:
        def height_(node: Node | None) -> int:
            if not node:
                return -1

            return max(
                1 + height_(node.left),
                1 + height_(node.right),
            )

        return height_(self.root)


test_case = TestCase()

# Insert
bst = BST()
bst.insert(8)
bst.insert(10)
bst.insert(3)
bst.insert(1)
test_case.assertEqual({1, 3, 8, 10}, bst.to_set())

# Search
bst = BST([8, 10, 3, 1])
test_case = TestCase()
test_case.assertEqual(True, bst.search(3))
test_case.assertEqual(False, bst.search(99))

# DFS
bst = BST([8, 10, 3, 1])
test_case.assertEqual(bst.to_list_df(), [1, 3, 8, 10])

# BFS
bst = BST([8, 10, 3, 1])
test_case.assertEqual(bst.to_list_bf(), [8, 3, 10, 1])

# Height
bst = BST([8, 10, 3, 1])
test_case.assertEqual(bst.height(), 2)
