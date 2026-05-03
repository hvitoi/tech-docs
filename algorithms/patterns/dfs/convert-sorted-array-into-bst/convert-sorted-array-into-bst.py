# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/ - 11k likes (Apr/2026)

# %%
from __future__ import annotations

from collections import deque
from dataclasses import dataclass


@dataclass
class Node:
    num: int
    left: Node | None = None
    right: Node | None = None


def serialize(root: Node | None) -> list[int | None]:
    """
    Serialize the BST into a list with Level-order
    """
    acc = []

    queue: deque[Node | None] = deque([root]) if root else deque()
    while queue:
        node = queue.popleft()

        if not node:
            acc.append(None)
            continue

        acc.append(node.num)

        queue.append(node.left)
        queue.append(node.right)

    while acc[-1] is None:
        acc.pop()

    return acc


def create_balanced_bst(nums: list[int]) -> Node | None:
    """
    Insert elements to the BST in an optimal order so that the tree has the minimum height possible
    """

    if not nums:
        return None

    mid = len(nums) // 2

    node = Node(nums[mid])
    node.left = create_balanced_bst(nums[:mid])
    node.right = create_balanced_bst(nums[mid + 1 :])

    return node


assert serialize(create_balanced_bst([1, 2, 3, 4, 5, 6, 7])) == [4, 2, 6, 1, 3, 5, 7]
assert serialize(create_balanced_bst([-10, -3, 0, 5, 9])) == [0, -3, 9, -10, None, 5]
assert serialize(create_balanced_bst([1, 3])) == [3, 1]
