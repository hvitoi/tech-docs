# https://leetcode.com/problems/validate-binary-search-tree/ - 18k likes (Apr/2026)

# %%
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    data: int
    left: Node | None = None
    right: Node | None = None


def is_valid_bst(node: Node, *, min=float("-inf"), max=float("inf")) -> bool:
    if (node.data < min) or (node.data > max):
        return False

    if node.left and not is_valid_bst(node.left, min=min, max=node.data):
        return False

    if node.right and not is_valid_bst(node.right, min=node.data, max=max):
        return False

    return True


node = Node(
    2,
    left=Node(1),
    right=Node(3),
)
assert is_valid_bst(node) is True

node = Node(
    5,
    left=Node(1),
    right=Node(
        4,
        left=Node(3),
        right=Node(6),
    ),
)
assert is_valid_bst(node) is False
