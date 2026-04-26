# %%
from __future__ import annotations

import collections
from dataclasses import dataclass, field


@dataclass
class Node[T]:
    data: T
    children: list[Node[T]] = field(default_factory=list)


def traverse_bf(node: Node):
    queue = collections.deque()
    queue.append(node)

    while queue:
        node = queue.popleft()
        print(node.data)
        queue.extend(node.children)


def traverse_df(node: Node):
    print(node.data)
    for child_node in node.children:
        traverse_df(child_node)


root = Node("a")
root.children.append(Node("b"))
root.children.append(Node("c"))
root.children.append(Node("d"))

root.children[0].children.append(Node("e"))
root.children[1].children.append(Node("f"))
root.children[1].children.append(Node("g"))
root.children[2].children.append(Node("h"))

traverse_bf(root)
print("---")
traverse_df(root)
