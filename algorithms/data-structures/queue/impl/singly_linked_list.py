# %%
from __future__ import annotations  # Allows self referencing in a class

from dataclasses import dataclass


@dataclass
class Node[T]:
    val: T
    next: Node[T] | None = None


class SinglyLinkedList[T]:
    def __init__(
        self,
        elements: list[T] | None = None,
    ):
        self.head: Node[T] | None = None

        if elements is None:
            elements = []

        for el in reversed(elements):
            self.push_left(el)

    def push_left(self, val: T) -> None:
        """
        O(1)
        """
        new_node = Node(val, self.head)  # new head
        self.head = new_node

    def pop_left(self) -> T:
        """
        O(1)
        """
        if not self.head:
            raise IndexError("empty list")

        popped = self.head
        self.head = popped.next
        return popped.val

    def push_right(self, val: T) -> None:
        """
        O(n)
        """
        new_node = Node(val)  # new tail

        if not self.head:
            self.head = new_node
            return

        it = self.head
        while it.next:
            it = it.next

        it.next = new_node

    def pop_right(self) -> T:
        """
        O(n)
        """
        if not self.head:
            raise IndexError("empty list")

        if not self.head.next:
            popped = self.head
            self.head = None
            return popped.val

        it = self.head
        while it.next and it.next.next:
            it = it.next

        assert it.next is not None
        popped = it.next
        it.next = None
        return popped.val

    def to_list(self) -> list[T]:
        acc = []
        it = self.head
        while it:
            acc.append(it.val)
            it = it.next
        return acc

    def to_list_recursively(self) -> list[T]:
        def to_list(node: Node[T] | None):
            if not node:
                return []
            return [node.val] + to_list(node.next)

        return to_list(self.head)


ll = SinglyLinkedList()
assert ll.to_list() == []

ll.push_left("a")
assert ll.to_list() == ["a"]

ll.push_left("b")
assert ll.to_list() == ["b", "a"]
assert ll.to_list_recursively() == ["b", "a"]

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
