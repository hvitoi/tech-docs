# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/ - 16k likes (Apr/2026)
# %%
from __future__ import annotations

import json
from dataclasses import dataclass


@dataclass
class Node:
    num: int
    left: Node | None = None
    right: Node | None = None


def to_dict(node: Node | None) -> dict[int, list[Node]]:
    if not node:
        return {}

    serialized = {node.num: []}

    left_serialized = to_dict(node.left)
    if left_serialized:
        serialized[node.num].append(left_serialized)

    right_serialized = to_dict(node.right)
    if right_serialized:
        serialized[node.num].append(right_serialized)

    return serialized


def pretty_print(node: Node | None) -> None:
    indented = json.dumps(to_dict(node), indent=2)
    print(indented)


def build_tree(preorder: list[int], inorder: list[int]) -> Node | None:
    if not inorder:
        return None

    root_val = preorder.pop(0)
    root = Node(root_val)
    root_index = inorder.index(root_val)

    root.left = build_tree(preorder, inorder[:root_index])
    root.right = build_tree(preorder, inorder[root_index + 1 :])

    return root


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
