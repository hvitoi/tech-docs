# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/ - 16k likes (Apr/2026)
# %%
from __future__ import annotations

import json
from dataclasses import dataclass


@dataclass
class Node:
    val: int
    left: Node | None = None
    right: Node | None = None


def to_dict(node: Node | None) -> dict[int, list[Node]]:
    if not node:
        return {}

    serialized = {node.val: []}

    left_serialized = to_dict(node.left)
    if left_serialized:
        serialized[node.val].append(left_serialized)

    right_serialized = to_dict(node.right)
    if right_serialized:
        serialized[node.val].append(right_serialized)

    return serialized


def pretty_print(node: Node | None) -> None:
    indented = json.dumps(to_dict(node), indent=2)
    print(indented)


def build_tree(preorder: list[int], inorder: list[int]) -> Node | None:
    """
    Get elements from the pre-order list, but use the in-order list to know when to stop for each node
    """
    in_index = {v: i for i, v in enumerate(inorder)}
    pre_iter = iter(preorder)

    def build(lo: int, hi: int) -> Node | None:
        if lo > hi:
            return None
        root = Node(next(pre_iter))
        mid = in_index[root.val]
        root.left = build(lo, mid - 1)
        root.right = build(mid + 1, hi)
        return root

    return build(0, len(inorder) - 1)


assert to_dict(
    build_tree(
        [3, 9, 20, 15, 7],
        [9, 3, 15, 20, 7],
    )
) == {
    3: [
        {9: []},
        {
            20: [
                {15: []},
                {7: []},
            ]
        },
    ]
}
