# %%
from unittest import TestCase
from typing import Self


class Node:
    def __init__(self, data: object, next: Self = None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self, elements: list = None):
        self.head: Node = None

        if elements is None:
            elements = []

        for el in reversed(elements):
            self.push_left(el)

    def push_left(self, data: object) -> None:
        new_node = Node(data, self.head)
        self.head = new_node

    def pop_left(self) -> object:
        if not self.head:
            return

        popped = self.head
        self.head = popped.next
        return popped.data

    def push_right(self, data: object) -> None:
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = new_node

    def pop_right(self) -> object:
        if not self.head:
            return

        if not self.head.next:
            popped = self.head
            self.head = None
            return popped.data

        itr = self.head
        while itr.next:
            if not itr.next.next:
                popped = itr.next
                itr.next = None
                return popped.data
            itr = itr.next

    def to_list(self):
        acc = []
        itr = self.head
        while itr:
            acc.append(itr.data)
            itr = itr.next
        return acc

    def to_list_recursively(self):
        def to_list(node: Node):
            if not node:
                return []
            return [node.data] + to_list(node.next)

        return to_list(self.head)


test_case = TestCase()

ll = SinglyLinkedList()
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
test_case.assertEqual(ll.to_list_recursively(), ["b", "a"])

ll.pop_left()
ll.pop_left()
test_case.assertEqual(ll.to_list(), [])
test_case.assertEqual(ll.to_list_recursively(), [])


# %%
def reverse(ll: SinglyLinkedList) -> SinglyLinkedList:
    reversed_list = SinglyLinkedList()
    curr = ll.head
    while curr:
        reversed_list.push_left(curr.data)
        curr = curr.next
    return reversed_list


ll = SinglyLinkedList([1, 2, 3])
reverse(ll).traverse()


# %%
def reverse_in_place(ll: SinglyLinkedList) -> SinglyLinkedList:
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


ll = SinglyLinkedList([1, 2, 3, 4, 5])
reverse_in_place(ll)
ll.traverse()


# %%
def reverse_in_place_recursively(ll: SinglyLinkedList, prev=None) -> SinglyLinkedList:
    # Time: O(n)
    # Space: O(n) due to the callstack

    curr = ll.head

    next = curr.next

    curr.next = prev
    prev = curr

    # base case
    if next:
        ll.head = next
        reverse_in_place_recursively(ll, prev)
    else:
        curr = prev


ll = SinglyLinkedList([1, 2, 3, 4, 5])
reverse_in_place_recursively(ll)
ll.traverse()


# %%
def reversed_list_head(head: Node) -> Node:
    if head is None or head.next is None:
        return head

    rest_reversed = reversed_list_head(head.next)
    head.next.next = head  # modify the tail of the rest_reversed
    head.next = None  # point the new tail of the rest_reversed to null because we don't know yet if it is the last one
    return rest_reversed


def reverse_in_place_recursively2(ll: SinglyLinkedList):
    ll.head = reversed_list_head(ll.head)
    return ll.head


ll = SinglyLinkedList([1, 2, 3, 4, 5])
reverse_in_place_recursively2(ll)
ll.traverse()
