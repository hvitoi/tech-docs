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
        if not elements:
            elements = []
        self.root = self.__deserialize(elements)

    def __deserialize(self, elements: list) -> Node | None:
        # copy the list do that the original one is not touched
        elements = elements.copy()

        def build_next_node() -> Node | None:
            el = elements.pop(0) if elements else None
            if el is not None:
                return Node(el)

        root = build_next_node()

        if root is None:
            return

        queue = deque([root])

        while elements:
            node = queue.popleft()

            node.left = build_next_node()
            if node.left:
                queue.append(node.left)

            node.right = build_next_node()
            if node.right:
                queue.append(node.right)

        return root


def memoize(fn):
    cache = {}

    def lookup_or_miss(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]

    return lookup_or_miss


def is_balanced(tree: BST) -> bool:
    @memoize
    def height(node: Node | None) -> int:
        if not node:
            return -1

        return max(
            1 + height(node.left),
            1 + height(node.right),
        )

    def _is_balanced(node: Node | None) -> bool:
        if not node:
            return True

        is_left_balanced = _is_balanced(node.left)
        if not is_left_balanced:
            return False

        is_right_balanced = _is_balanced(node.right)
        if not is_right_balanced:
            return False

        left_height = height(node.left)
        right_height = height(node.right)

        return abs(left_height - right_height) <= 1

    return _is_balanced(tree.root)


def is_balanced2(tree: BST) -> bool:
    def check_balance(node: Node | None) -> tuple[bool, int]:
        """
        Returns whether a node is balanced and what is its height
        """
        if not node:
            return (True, -1)

        is_left_balanced, left_height = check_balance(node.left)
        if not is_left_balanced:
            return (False, 1 + left_height)

        is_right_balanced, right_height = check_balance(node.right)
        if not is_right_balanced:
            return (False, 1 + right_height)

        am_i_balanced = abs(left_height - right_height) <= 1
        return (am_i_balanced, 1 + max(left_height, right_height))

    return check_balance(tree.root)[0]


test_case = TestCase()

for fn in {is_balanced, is_balanced2}:
    test_case.assertEqual(fn(BST([3, 9, 20, None, None, 15, 7])), True)
    test_case.assertEqual(fn(BST([1, 2, 2, 3, 3, None, None, 4, 4])), False)
