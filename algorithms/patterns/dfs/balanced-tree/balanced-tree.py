# https://leetcode.com/problems/balanced-binary-tree/ - 12k likes (Apr/2026)
# %%
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    data: int
    left: Node | None = None
    right: Node | None = None


def is_balanced(node: Node | None) -> bool:
    def height(node: Node | None) -> int:
        if node is None:
            return -1
        return 1 + max(height(node.left), height(node.right))

    if node is None:
        return True

    if not is_balanced(node.left):
        return False

    if not is_balanced(node.right):
        return False

    left_height = height(node.left)
    right_height = height(node.right)

    return abs(left_height - right_height) <= 1


bst = Node(3, left=Node(9), right=Node(20, left=Node(15), right=Node(7)))
assert is_balanced(bst) is True

bst = Node(
    1,
    left=Node(2, left=Node(3, left=Node(4), right=Node(4)), right=Node(3)),
    right=Node(2),
)
assert is_balanced(bst) is False
