# %%
import json


class TreeNode:
    def __init__(self, val, *, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def to_dict(self, node=None, acc=None):
        node = node if node else self
        acc = acc if acc is not None else {}

        if not node:
            return None

        acc[node.val] = []

        if node.left:
            acc[node.val].append(self.to_dict(node.left))

        if node.right:
            acc[node.val].append(self.to_dict(node.right))

        return acc

    def pretty_print(self):
        indented = json.dumps(self.to_dict(), indent=2)
        print(indented)


def build_tree(preorder: list, inorder: list) -> TreeNode:
    if inorder:
        root_val = preorder.pop(0)
        root = TreeNode(root_val)

        root_index = inorder.index(root_val)

        root.left = build_tree(preorder, inorder[:root_index])
        root.right = build_tree(preorder, inorder[root_index + 1 :])

        return root


tree = build_tree(
    [3, 9, 20, 15, 7],
    [9, 3, 15, 20, 7],
)

tree.pretty_print()
