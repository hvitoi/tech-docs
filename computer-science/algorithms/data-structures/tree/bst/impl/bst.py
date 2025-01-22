# %%
import unittest
import collections


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BST:
    def __init__(self, elements: list | None = None):
        self.root = self._deserialize(elements)

    def _deserialize(self, elements: list) -> Node:
        """
        Create a BST out of a serialized BST as a list. E.g., [3, 9, 20, None, None, 15, 7]
        The serialized format uses BFS, therefore this algorithm uses Bread-First Traversal to deserialize it
        """
        if not elements:
            return

        remaining_elements = collections.deque(elements)
        root = Node(remaining_elements.popleft())
        nodes = collections.deque([root])

        while remaining_elements:
            node = nodes.popleft()

            # child may be None if there are no remaining elements or if the next element is None
            left_child = remaining_elements.popleft() if remaining_elements else None
            if left_child:
                node.left = Node(left_child)
                nodes.append(node.left)

            right_child = remaining_elements.popleft() if remaining_elements else None
            if right_child:
                node.right = Node(right_child)
                nodes.append(node.right)

        return root

    def serialize(self) -> list[int | None]:
        """
        Serialize the BST into a list created via Bread-first Traversal
        """
        acc = []

        nodes = collections.deque([self.root]) if self.root else collections.deque()
        while nodes:
            node = nodes.popleft()

            # It's necessary to do this verification here because the node (left or right) inserted into the nodes queue may be None
            if not node:
                acc.append(None)
                continue

            acc.append(node.data)
            nodes.append(node.left)
            nodes.append(node.right)

        # trim right Nones
        while acc[-1] is None:
            acc.pop()

        return acc

    def insert(self, value: int) -> None:
        """
        Insert an element to the BST
        """

        def _insert(node: Node, value: int) -> None:
            if value == node.data:
                raise Exception("Duplicated value")

            if value < node.data:
                if node.left:
                    _insert(node.left, value)
                else:
                    node.left = Node(value)

            if value > node.data:
                if node.right:
                    _insert(node.right, value)
                else:
                    node.right = Node(value)

        if not self.root:
            self.root = Node(value)
            return

        _insert(self.root, value)

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

    def to_list_df(self) -> list[int]:
        """
        Depth-First In-Order Traversal
        """

        def dfs(node: Node | None) -> list[int]:
            acc = []

            if not node:
                return acc

            acc.extend(dfs(node.left))
            acc.append(node.data)  # in-order
            acc.extend(dfs(node.right))

            return acc

        return dfs(self.root)

    def to_list_bf(self) -> list[int]:
        """
        Breadth-First Traversal
        """

        def bfs(root: Node | None) -> list[int]:
            acc = []

            if not root:
                return acc

            nodes = collections.deque([root])

            while nodes:
                node = nodes.popleft()
                acc.append(node.data)

                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)

            return acc

        return bfs(self.root)

    def height_df(self, target: int | None = None) -> int:
        """
        Height of a node/tree using DFS
        """

        def height_total(node) -> int:
            if not node:
                return -1

            return max(
                1 + height_total(node.left),
                1 + height_total(node.right),
            )

        def height_for_element(node, target) -> int:
            if not node:
                return -1

            if node.data == target:
                return 0

            # search left
            search = height_for_element(node.left, target)
            if search != -1:
                return 1 + search

            # search right
            search = height_for_element(node.right, target)
            if search != -1:
                return 1 + search

            # if element was not found anywhere
            return -1

        if target:
            return height_for_element(self.root, target)
        else:
            return height_total(self.root)

    def height_bf(self, target: int | None = None) -> int:
        """
        Height of a node/tree using BFS
        """

        def total_height(root) -> int:
            if not root:
                return -1

            queue = collections.deque([(root, 0)])

            while queue:
                node, level = queue.popleft()

                if node.left:
                    queue.append((node.left, level + 1))

                if node.right:
                    queue.append((node.right, level + 1))

            return level

        def height_for_element(root, target) -> int:
            height = -1

            if not root:
                return height

            queue = collections.deque([(root, 0)])

            while queue:
                node, level = queue.popleft()

                if node.data == target:
                    height = level
                    break

                if node.left:
                    queue.append((node.left, level + 1))

                if node.right:
                    queue.append((node.right, level + 1))

            return height

        if target:
            return height_for_element(self.root, target)
        else:
            return total_height(self.root)


test_case = unittest.TestCase()


# Serialize / Deserialize
serialized_bst = [3, 9, 20, None, None, 15, 7]
bst = BST(serialized_bst)
test_case.assertEqual(bst.serialize(), serialized_bst)

# Insert
bst = BST()
bst.insert(1)
bst.insert(2)
test_case.assertEqual(bst.serialize(), [1, None, 2])

# Search
bst = BST([50, 30, 70, 20, 40, 60, 80, 10])
test_case.assertEqual(True, bst.search(60))
test_case.assertEqual(False, bst.search(99))

# To List (DF)
bst = BST([50, 30, 70, 20, 40, 60, 80, 10])
test_case.assertEqual(bst.to_list_df(), [10, 20, 30, 40, 50, 60, 70, 80])

# To List (BF)
bst = BST([50, 30, 70, 20, 40, 60, 80, 10])
test_case.assertEqual(bst.to_list_bf(), [50, 30, 70, 20, 40, 60, 80, 10])

# Height (DF)
bst = BST([50, 30, 70, 20, 40, 60, 80, 10])
test_case.assertEqual(bst.height_df(), 3)
test_case.assertEqual(bst.height_df(99), -1)
test_case.assertEqual(bst.height_df(50), 0)
test_case.assertEqual(bst.height_df(30), 1)
test_case.assertEqual(bst.height_df(20), 2)
test_case.assertEqual(bst.height_df(10), 3)

# Height (BF)
bst = BST([50, 30, 70, 20, 40, 60, 80, 10])
test_case.assertEqual(bst.height_bf(), 3)
test_case.assertEqual(bst.height_bf(99), -1)
test_case.assertEqual(bst.height_bf(50), 0)
test_case.assertEqual(bst.height_bf(30), 1)
test_case.assertEqual(bst.height_bf(20), 2)
test_case.assertEqual(bst.height_bf(10), 3)
