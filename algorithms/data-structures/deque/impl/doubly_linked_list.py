# %%
from __future__ import annotations  # Allows self referencing in a class

from dataclasses import dataclass


@dataclass
class Node[T]:
    val: T
    next: Node | None = None
    prev: Node | None = None


class DoublyLinkedList[T]:
    def __init__(self, elements: list[T] | None = None):
        self.head: Node | None = None
        self.tail: Node | None = None

        if elements is None:
            elements = []

        for el in elements:
            self.push_right(el)

    def push_left(self, val: T) -> None:
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def pop_left(self) -> T:
        if not self.head:
            raise IndexError("empty list")

        if not self.head.next:
            popped = self.head
            self.head = None
            self.tail = None
            return popped.val

        popped = self.head
        self.head = popped.next
        self.head.prev = None
        return popped.val

    def push_right(self, val: T) -> None:
        new_node = Node(val)

        if not self.tail:
            self.tail = new_node
            self.head = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def pop_right(self) -> T:
        if not self.tail:
            raise IndexError("empty list")

        if not self.tail.prev:
            popped = self.tail
            self.head = None
            self.tail = None
            return popped.val

        popped = self.tail
        self.tail = popped.prev
        self.tail.next = None
        return popped.val

    def to_list(self) -> list[T]:
        acc = []
        curr = self.head
        while curr:
            acc.append(curr.val)
            curr = curr.next
        return acc

    def to_list_inverse(self) -> list:
        acc = []
        curr = self.tail
        while curr:
            acc.append(curr.val)
            curr = curr.prev
        return acc


ll = DoublyLinkedList()
assert ll.to_list() == []

ll.push_left("a")
assert ll.to_list() == ["a"]

ll.push_left("b")
assert ll.to_list() == ["b", "a"]

assert ll.pop_left() == "b"
assert ll.to_list() == ["a"]

assert ll.pop_left() == "a"
assert ll.to_list() == []

try:
    ll.pop_left()
    assert False, "expected IndexError"
except IndexError:
    pass
assert ll.to_list() == []
assert ll.to_list() == []

##

ll.push_right("a")
assert ll.to_list() == ["a"]

ll.push_right("b")
assert ll.to_list() == ["a", "b"]

assert ll.pop_right() == "b"
assert ll.to_list() == ["a"]

assert ll.pop_right() == "a"
assert ll.to_list() == []

try:
    ll.pop_right()
    assert False, "expected IndexError"
except IndexError:
    pass
assert ll.to_list() == []

##
ll.push_left("a")
ll.push_left("b")
assert ll.to_list() == ["b", "a"]
assert ll.to_list_inverse() == ["a", "b"]

ll.pop_left()
ll.pop_left()
assert ll.to_list() == []
assert ll.to_list_inverse() == []
