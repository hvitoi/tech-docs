# %%
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node[T]:
    data: T
    next: Node[T] | None = None


class LinkedList[T]:
    def __init__(self, elements: list[T] | None = None):
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
    col1: LinkedList[int],
    col2: LinkedList[int],
) -> LinkedList[int]:

    merged: LinkedList[int] = LinkedList()

    curr1: Node[int] | None = col1.head
    curr2: Node[int] | None = col2.head

    while curr1 or curr2:
        el1 = curr1.data if curr1 is not None else float("inf")
        el2 = curr2.data if curr2 is not None else float("inf")

        if el1 <= el2:
            merged.add(el1)
            curr1 = curr1.next
        else:
            merged.add(el2)
            curr2 = curr2.next

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


col1 = LinkedList([1, 2, 4])
col2 = LinkedList([1, 3, 4])
assert merge(col1, col2).to_list() == [1, 1, 2, 3, 4, 4]


col1 = LinkedList([])
col2 = LinkedList([])
assert merge(col1, col2).to_list() == []

col1 = LinkedList([])
col2 = LinkedList([0])
assert merge(col1, col2).to_list() == [0]
