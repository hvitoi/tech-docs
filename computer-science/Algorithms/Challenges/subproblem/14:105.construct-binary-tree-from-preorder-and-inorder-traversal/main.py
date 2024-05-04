# %%
import json
from unittest import TestCase


class TreeNode:
    def __init__(self, val, *, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def to_dict(self):
        def _to_dict(node):
            if not node:
                return {}

            serialized = {node.val: []}

            left_serialized = _to_dict(node.left)
            if left_serialized:
                serialized[node.val].append(left_serialized)

            right_serialized = _to_dict(node.right)
            if right_serialized:
                serialized[node.val].append(right_serialized)

            return serialized

        return _to_dict(self)

    def pretty_print(self):
        indented = json.dumps(self.to_dict(), indent=2)
        print(indented)


def build_tree(preorder: list, inorder: list) -> TreeNode | None:
    if not inorder:
        return None

    root_val = preorder.pop(0)
    root = TreeNode(root_val)

    root_index = inorder.index(root_val)

    root.left = build_tree(preorder, inorder[:root_index])
    root.right = build_tree(preorder, inorder[root_index + 1 :])

    return root


test_case = TestCase()
test_case.assertEqual(
    build_tree(
        [3, 9, 20, 15, 7],
        [9, 3, 15, 20, 7],
    ).to_dict(),
    {3: [{9: []}, {20: [{15: []}, {7: []}]}]},
)
