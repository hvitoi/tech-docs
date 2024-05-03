# %%
from typing import Self
from unittest import TestCase


class Node:
    def __init__(self, data: object, *, next: Self = None, prev: Self = None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self, elements: list = None):
        self.head: Node = None
        self.tail: Node = None

        if elements is None:
            elements = []

        for el in elements:
            self.push_right(el)

    def push_left(self, data: object) -> None:
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def pop_left(self) -> object:
        if not self.head:
            return

        if not self.head.next:
            popped = self.head
            self.head = None
            self.tail = None
            return popped.data

        popped = self.head
        self.head = popped.next
        self.head.prev = None
        return popped.data

    def push_right(self, data: object) -> None:
        new_node = Node(data)

        if not self.tail:
            self.tail = new_node
            self.head = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def pop_right(self) -> object:
        if not self.tail:
            return

        if not self.tail.prev:
            popped = self.tail
            self.head = None
            self.tail = None
            return popped.data

        popped = self.tail
        self.tail = popped.prev
        self.tail.next = None
        return popped.data

    def to_list(self) -> list:
        acc = []
        itr = self.head
        while itr:
            acc.append(itr.data)
            itr = itr.next
        return acc

    def to_list_inverse(self) -> list:
        acc = []
        itr = self.tail
        while itr:
            acc.append(itr.data)
            itr = itr.prev
        return acc


test_case = TestCase()

ll = DoublyLinkedList()
test_case.assertEqual(ll.to_list(), [])

ll.push_left("a")
test_case.assertEqual(ll.to_list(), ["a"])

ll.push_left("b")
test_case.assertEqual(ll.to_list(), ["b", "a"])

test_case.assertEqual(ll.pop_left(), "b")
test_case.assertEqual(ll.to_list(), ["a"])

test_case.assertEqual(ll.pop_left(), "a")
test_case.assertEqual(ll.to_list(), [])

test_case.assertEqual(ll.pop_left(), None)
test_case.assertEqual(ll.to_list(), [])

##

ll.push_right("a")
test_case.assertEqual(ll.to_list(), ["a"])

ll.push_right("b")
test_case.assertEqual(ll.to_list(), ["a", "b"])

test_case.assertEqual(ll.pop_right(), "b")
test_case.assertEqual(ll.to_list(), ["a"])

test_case.assertEqual(ll.pop_right(), "a")
test_case.assertEqual(ll.to_list(), [])

test_case.assertEqual(ll.pop_right(), None)
test_case.assertEqual(ll.to_list(), [])

##
ll.push_left("a")
ll.push_left("b")
test_case.assertEqual(ll.to_list(), ["b", "a"])
test_case.assertEqual(ll.to_list_inverse(), ["a", "b"])

ll.pop_left()
ll.pop_left()
test_case.assertEqual(ll.to_list(), [])
test_case.assertEqual(ll.to_list_inverse(), [])
