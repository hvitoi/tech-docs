# %%
from __future__ import annotations  # Allows self referencing in a class

from dataclasses import dataclass


@dataclass
class Node[T]:
    data: T
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

    def push_left(self, data: T) -> None:
        """
        O(1)
        """
        new_node = Node(data, self.head)  # new head
        self.head = new_node

    def pop_left(self) -> T:
        """
        O(1)
        """
        if not self.head:
            raise IndexError("empty list")

        popped = self.head
        self.head = popped.next
        return popped.data

    def push_right(self, data: T) -> None:
        """
        O(n)
        """
        new_node = Node(data)  # new tail

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
            return popped.data

        it = self.head
        while it.next and it.next.next:
            it = it.next

        assert it.next is not None
        popped = it.next
        it.next = None
        return popped.data

    def to_list(self) -> list[T]:
        acc = []
        it = self.head
        while it:
            acc.append(it.data)
            it = it.next
        return acc

    def to_list_recursively(self) -> list[T]:
        def to_list(node: Node[T] | None):
            if not node:
                return []
            return [node.data] + to_list(node.next)

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


# %%
def reverse(ll: SinglyLinkedList) -> None:
    # Time: O(n)
    # Space: O(1)
    curr = ll.head
    prev = None  # the previous item has to be remembered because on a linked list you can't access the previous element

    while curr:
        # stash the next element so that we can traverse the original list
        next = curr.next

        # switch the pointer direction
        curr.next = prev
        prev = curr

        # jump to the next element in the original list
        curr = next

    ll.head = prev


ll = SinglyLinkedList([1, 2, 3])
reverse(ll)
assert ll.to_list() == [3, 2, 1]

ll = SinglyLinkedList([1])
reverse(ll)
assert ll.to_list() == [1]

ll = SinglyLinkedList()
reverse(ll)
assert ll.to_list() == []


# %%
def reverse_in_place_recursively2(ll: SinglyLinkedList) -> None:
    def reversed_list_head(head: Node) -> Node:
        """Returns the head of the reversed linked list"""
        if head is None or head.next is None:
            return head

        rest_reversed = reversed_list_head(head.next)
        head.next.next = head  # modify the tail of the rest_reversed
        head.next = None  # point the new tail of the rest_reversed to null because we don't know yet if it is the last one
        return rest_reversed

    ll.head = reversed_list_head(ll.head)


ll = SinglyLinkedList([1, 2, 3])
reverse(ll)
assert ll.to_list() == [3, 2, 1]

ll = SinglyLinkedList([1])
reverse(ll)
assert ll.to_list() == [1]

ll = SinglyLinkedList()
reverse(ll)
assert ll.to_list() == []
