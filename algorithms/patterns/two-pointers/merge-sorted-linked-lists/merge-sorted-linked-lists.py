# %%
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node[T]:
    data: T
    next: Node[T] | None = None


class LinkedList[T]:
    def __init__(self, elements: list[T] | None = None) -> None:
        self.head: Node[T] | None = None
        if elements:
            for el in reversed(elements):
                self.add(el)

    def add(self, el: T) -> None:
        new_node = Node(el)
        new_node.next = self.head
        self.head = new_node

    def to_list(self) -> list[T]:
        acc: list[T] = []
        curr = self.head
        while curr:
            acc.append(curr.data)
            curr = curr.next
        return acc


def merge(
    l1: LinkedList[int],
    l2: LinkedList[int],
) -> LinkedList[int]:

    merged: LinkedList[int] = LinkedList()

    h1: Node[int] | None = l1.head
    h2: Node[int] | None = l2.head

    while h1 or h2:
        el1 = h1.data if h1 is not None else float("inf")
        el2 = h2.data if h2 is not None else float("inf")

        if el1 <= el2:
            merged.add(el1)
            h1 = h1.next
        else:
            merged.add(el2)
            h2 = h2.next

    # reverse the Linked List (see "reverse-linked-list.py")
    curr: Node[int] | None = merged.head
    prev: Node[int] | None = None
    while curr:
        # stash before overwrite
        nxt = curr.next

        # flip the link
        curr.next = prev

        # advance window
        prev = curr
        curr = nxt
    merged.head = prev

    return merged


def merge_reuse_nodes(
    l1: LinkedList[int],
    l2: LinkedList[int],
) -> LinkedList[int]:
    """O(n + m) time, O(1) extra space — splices existing nodes.

    Note: l1 and l2 are consumed; their nodes are now part of the result.
    The original lists are destroyed/corrupted, their nodes have been spliced/rewired
    """

    dummy_head: Node[int] = Node(0)  # sentinel head, simplifies the first append
    tail = dummy_head  # hold a tail pointer, and append to it, this way the list is already inverted
    h1, h2 = l1.head, l2.head

    while h1 and h2:
        if h1.data <= h2.data:
            tail.next = h1  # splice — reuse existing node
            h1 = h1.next
        else:
            tail.next = h2
            h2 = h2.next
        tail = tail.next

    tail.next = h1 or h2  # attach the remainder in one move

    result: LinkedList[int] = LinkedList()
    result.head = dummy_head.next  # drop the dummy head
    return result


for fn in [merge, merge_reuse_nodes]:
    col1 = LinkedList([1, 2, 4])
    col2 = LinkedList([1, 3, 4])
    assert fn(col1, col2).to_list() == [1, 1, 2, 3, 4, 4]

    col1 = LinkedList([])
    col2 = LinkedList([])
    assert fn(col1, col2).to_list() == []

    col1 = LinkedList([])
    col2 = LinkedList([0])
    assert fn(col1, col2).to_list() == [0]
