# %%
from __future__ import annotations

from collections import deque
from collections.abc import Iterator
from dataclasses import dataclass, field


@dataclass
class Node[T]:
    data: T
    children: list[Node[T]] = field(default_factory=list)


def traverse_level_order[T](node: Node[T]) -> Iterator[T]:
    """
    Performs a Level-order (breath-first) traversal
    """
    queue = deque([node])
    while queue:
        curr = queue.popleft()
        yield curr.data
        queue.extend(curr.children)


def traverse_pre_order[T](node: Node[T]) -> Iterator[T]:
    """
    Performs a Pre-order (depth-first) traversal
    """
    yield node.data
    for child in node.children:
        yield from traverse_pre_order(child)


root = Node(
    "a",
    [
        Node("b", [Node("e")]),
        Node("c", [Node("f"), Node("g")]),
        Node("d", [Node("e")]),
    ],
)
#     a
#   / | \
#  b  c  d
#  |  |\ |
#  e  f g e


print(list(traverse_level_order(root)))
print(list(traverse_pre_order(root)))
