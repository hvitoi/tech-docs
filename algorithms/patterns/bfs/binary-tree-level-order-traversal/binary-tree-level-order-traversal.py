# %%
from __future__ import annotations

from collections import deque
from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class Node[T]:
    data: T
    left: Node[T] | None = None
    right: Node[T] | None = None


def traverse_level_order[T](node: Node[T]) -> Iterator[T]:
    """
    Performs a Level-order (breath-first) traversal
    """
    queue = deque([node])
    while queue:
        curr = queue.popleft()
        if not curr:
            continue
        yield curr.data
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)


#    3
#   / \
#  9  20
#     / \
#    15  7
root = Node(3, left=Node(9), right=Node(20, left=Node(15), right=Node(7)))
assert list(traverse_level_order(root)) == [3, 9, 20, 15, 7]

root = Node(1)
assert list(traverse_level_order(root)) == [1]

root = None
assert list(traverse_level_order(root)) == []
