# %%
from functools import reduce
from unittest import TestCase


class LinkedListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, elements: list = None):
        self.head = None
        if elements:
            for el in reversed(elements):
                self.insert(el)

    def insert(self, val) -> None:
        new_node = LinkedListNode(val, self.head)
        self.head = new_node

    def remove(self):
        if not self.head:
            return None

        el = self.head.val
        self.head = self.head.next
        return el

    def peek(self):
        return self.head

    def to_list(self):
        acc = []
        while self.peek():
            acc.append(self.remove())
        return list(acc)


def add_two_numbers_from_linked_list(
    ll1: LinkedListNode,
    ll2: LinkedListNode,
) -> LinkedListNode:
    num1 = ""
    while ll1.peek():
        num1 = str(ll1.remove()) + num1
    num1 = int(num1)

    num2 = ""
    while ll2.peek():
        num2 = str(ll2.remove()) + num2
    num2 = int(num2)

    num_sum = str(num1 + num2)
    result = LinkedList()
    for num in num_sum:
        result.insert(int(num))
    return result


test_case = TestCase()

test_case.assertEqual(
    add_two_numbers_from_linked_list(
        LinkedList([2, 4, 3]), LinkedList([5, 6, 4])
    ).to_list(),
    [7, 0, 8],
)
test_case.assertEqual(
    add_two_numbers_from_linked_list(LinkedList([0]), LinkedList([0])).to_list(),
    [0],
)
test_case.assertEqual(
    add_two_numbers_from_linked_list(
        LinkedList([9, 9, 9, 9, 9, 9, 9]), LinkedList([9, 9, 9, 9])
    ).to_list(),
    [8, 9, 9, 9, 0, 0, 0, 1],
)


# %%
# Variation 2: receive as inputs the lists
def add_two_numbers_from_list(l1, l2):
    num1 = reduce(lambda acc, el: int(str(el) + str(acc)), l1)
    num2 = reduce(lambda acc, el: int(str(el) + str(acc)), l2)

    return list(map(int, reversed(str(num1 + num2))))


test_case = TestCase()

test_case.assertEqual(
    add_two_numbers_from_list([2, 4, 3], [5, 6, 4]),
    [7, 0, 8],
)
test_case.assertEqual(
    add_two_numbers_from_list([0], [0]),
    [0],
)
test_case.assertEqual(
    add_two_numbers_from_list([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]),
    [8, 9, 9, 9, 0, 0, 0, 1],
)
