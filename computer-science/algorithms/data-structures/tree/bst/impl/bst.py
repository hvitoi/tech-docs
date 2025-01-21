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
        self.root = self.__deserialize(elements)

    def __deserialize(self, elements: list) -> Node:
        """
        Create a BST out of a serialized BST as a list. E.g., [3, 9, 20, None, None, 15, 7]
        Uses Bread-First Traversal
        """
        if not elements:
            return

        remaining_elements = deque(elements)
        root = Node(remaining_elements.popleft())
        nodes = deque([root])

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
        acc = []

        nodes = deque([self.root]) if self.root else deque()
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
        Depth-First Pre-Order Traversal (doesn't really matter since it's a set)
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
            acc.append(node.data)  # in-order
            acc.extend(dfs(node.right))

            return acc

        return dfs(self.root)

    def to_list_bf(self) -> list[int]:
        """
        Traverse Breadth-First and add elements to a list
        """

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

        return bfs(self.root)

    def height_df(self, target: int | None = None) -> int:
        """
        Height of a node/tree using DFS
        """

        def total_height(node) -> int:
            if not node:
                return -1

            return max(
                1 + total_height(node.left),
                1 + total_height(node.right),
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
            return total_height(self.root)

    def height_bf(self, target: int | None = None) -> int:
        """
        Height of a node/tree using BFS
        """

        def total_height(root) -> int:
            if not root:
                return -1

            queue: deque[tuple[Node, int]] = deque([(root, 0)])

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

            queue: deque[tuple[Node, int]] = deque([(root, 0)])

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


test_case = TestCase()


# Serialize / Deserialize
raw = [3, 9, 20, None, None, 15, 7]
a = BST(raw)
test_case.assertEqual(BST(raw).serialize(), raw)

# # Insert
# bst = BST()
# bst.insert(1)
# bst.insert(2)
# test_case.assertEqual(bst.to_set(), {1, 2})

# # Search
# bst = BST([50, 30, 70, 20, 40, 60, 80, 10])
# test_case.assertEqual(True, bst.search(60))
# test_case.assertEqual(False, bst.search(99))

# # To Set (DF)
# bst = BST([50, 30, 70, 20, 40, 60, 80, 10])
# test_case.assertEqual(bst.to_set(), {10, 20, 30, 40, 50, 60, 70, 80})

# # To List (DF)
# bst = BST([50, 30, 70, 20, 40, 60, 80, 10])
# test_case.assertEqual(bst.to_list_df(), [10, 20, 30, 40, 50, 60, 70, 80])

# # To List (BF)
# bst = BST([50, 30, 70, 20, 40, 60, 80, 10])
# test_case.assertEqual(bst.to_list_bf(), [50, 30, 70, 20, 40, 60, 80, 10])

# # Height (DF)
# bst = BST([50, 30, 70, 20, 40, 60, 80, 10])
# test_case.assertEqual(bst.height_df(), 3)
# test_case.assertEqual(bst.height_df(99), -1)
# test_case.assertEqual(bst.height_df(50), 0)
# test_case.assertEqual(bst.height_df(30), 1)
# test_case.assertEqual(bst.height_df(20), 2)
# test_case.assertEqual(bst.height_df(10), 3)

# # Height (BF)
# bst = BST([50, 30, 70, 20, 40, 60, 80, 10])
# test_case.assertEqual(bst.height_bf(), 3)
# test_case.assertEqual(bst.height_bf(99), -1)
# test_case.assertEqual(bst.height_bf(50), 0)
# test_case.assertEqual(bst.height_bf(30), 1)
# test_case.assertEqual(bst.height_bf(20), 2)
# test_case.assertEqual(bst.height_bf(10), 3)
