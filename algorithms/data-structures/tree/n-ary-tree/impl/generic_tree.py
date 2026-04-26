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


root = Node("a")
root.children.append(Node("b"))
root.children.append(Node("c"))
root.children.append(Node("d"))

root.children[0].children.append(Node("e"))
root.children[1].children.append(Node("f"))
root.children[1].children.append(Node("g"))
root.children[2].children.append(Node("h"))


print(list(traverse_level_order(root)))
print(list(traverse_pre_order(root)))
