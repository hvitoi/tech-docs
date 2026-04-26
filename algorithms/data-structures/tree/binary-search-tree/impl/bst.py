# %%
from __future__ import annotations

from collections import deque
from dataclasses import dataclass


@dataclass
class Node:
    num: int
    left: Node | None = None
    right: Node | None = None


class BST:
    def __init__(self, elements: list[int | None] | None = None):
        self.root: Node | None = self._deserialize(elements)

    def _deserialize(self, elements: list[int | None] | None) -> Node | None:
        """
        Create a BST out of a serialized BST as a list. E.g., [3, 9, 20, None, None, 15, 7]
        The serialized format uses Level-order, therefore this algorithm uses Bread-First Traversal to deserialize it
        """
        if not elements:
            return None

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
        """
        Serialize the BST into a list with Level-order
        """
        acc = []

        queue: deque[Node | None] = deque([self.root]) if self.root else deque()
        while queue:
            node = queue.popleft()

            # It's necessary to do this verification here because the node (left or right) inserted into the nodes queue may be None
            if not node:
                acc.append(None)
                continue

            acc.append(node.num)

            queue.append(node.left)
            queue.append(node.right)

        # trim right Nones
        while acc[-1] is None:
            acc.pop()

        return acc

    def insert(self, num: int) -> None:
        """
        Insert an element to the BST
        """

        def _insert(node: Node, num: int) -> None:
            if num == node.num:
                raise Exception("Duplicated value")

            if num < node.num:
                if node.left:
                    _insert(node.left, num)
                else:
                    node.left = Node(num)

            if num > node.num:
                if node.right:
                    _insert(node.right, num)
                else:
                    node.right = Node(num)

        if not self.root:
            self.root = Node(num)
            return

        _insert(self.root, num)

    def search(self, target: int) -> bool:
        """
        Returns whether an element is found in the tree
        """

        def search_(node: Node | None, target: int) -> bool:
            """Pre-Order (depth-First) Traversal"""
            if not node:
                return False

            if target == node.num:
                return True

            if target < node.num:
                return search_(node.left, target)

            if target > node.num:
                return search_(node.right, target)

            return False

        return search_(self.root, target)

    def to_list_in_order(self) -> list[int]:
        """
        In-Order Traversal (depth-first)
        """

        def recur(node: Node | None) -> list[int]:
            acc = []

            if not node:
                return acc

            acc.extend(recur(node.left))
            acc.append(node.num)  # in-order
            acc.extend(recur(node.right))

            return acc

        return recur(self.root)

    def to_list_level_order(self) -> list[int]:
        """
        Level-Order Traversal (Breadth-First)
        """

        def recur(root: Node | None) -> list[int]:
            acc = []

            if not root:
                return acc

            nodes = deque([root])

            while nodes:
                node = nodes.popleft()
                acc.append(node.num)

                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)

            return acc

        return recur(self.root)

    def height_df(self, target: int | None = None) -> int:
        """
        Height of a node/tree
        """

        def height_total(node: Node | None) -> int:
            if not node:
                return -1

            return max(
                1 + height_total(node.left),
                1 + height_total(node.right),
            )

        def height_for_element(node: Node | None, target: int) -> int:
            if not node:
                return -1

            if node.num == target:
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
        Height of a node/tree
        """

        def height_total(root: Node | None) -> int:
            if not root:
                return -1

            # the "nodes" queue stores the height of each node
            nodes: deque[tuple[Node, int]] = deque([(root, 0)])
            while nodes:
                node, level = nodes.popleft()

                if node.left:
                    nodes.append((node.left, level + 1))

                if node.right:
                    nodes.append((node.right, level + 1))

            # the level of the last node added via BFS
            return level

        def height_for_element(root: Node | None, target: int) -> int:
            if not root:
                return -1

            nodes = deque([(root, 0)])
            while nodes:
                node, level = nodes.popleft()

                if node.num == target:
                    return level

                if node.left:
                    nodes.append((node.left, level + 1))

                if node.right:
                    nodes.append((node.right, level + 1))

            # element not found
            return -1

        if target:
            return height_for_element(self.root, target)
        else:
            return height_total(self.root)


# Serialize / Deserialize
serialized_bst = [3, 9, 20, None, None, 15, 7]
bst = BST(serialized_bst)
assert bst.serialize() == serialized_bst

# Insert
bst = BST()
bst.insert(1)
bst.insert(2)
assert bst.serialize() == [1, None, 2]

# Search
bst = BST([50, 30, 70, 20, 40, 60, 80, 10])
assert bst.search(60) is True
assert bst.search(99) is False

# To List (DF)
bst = BST([50, 30, 70, 20, 40, 60, 80, 10])
assert bst.to_list_in_order() == [10, 20, 30, 40, 50, 60, 70, 80]

# To List (BF)
bst = BST([50, 30, 70, 20, 40, 60, 80, 10])
assert bst.to_list_level_order() == [50, 30, 70, 20, 40, 60, 80, 10]

# Height (DF)
bst = BST([50, 30, 70, 20, 40, 60, 80, 10])
assert bst.height_df() == 3
assert bst.height_df(99) == -1
assert bst.height_df(50) == 0
assert bst.height_df(30) == 1
assert bst.height_df(20) == 2
assert bst.height_df(10) == 3

# Height (BF)
bst = BST([50, 30, 70, 20, 40, 60, 80, 10])
assert bst.height_bf() == 3
assert bst.height_bf(99) == -1
assert bst.height_bf(50) == 0
assert bst.height_bf(30) == 1
assert bst.height_bf(20) == 2
assert bst.height_bf(10) == 3
