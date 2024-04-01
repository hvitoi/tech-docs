# %%
from functools import reduce
from unittest import TestCase


class LinkedListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1, l2):
    num1 = reduce(lambda acc, el: int(str(el) + str(acc)), l1)
    num2 = reduce(lambda acc, el: int(str(el) + str(acc)), l2)

    return list(map(int, reversed(str(num1 + num2))))


test_case = TestCase()

test_case.assertEqual(add_two_numbers([2, 4, 3], [5, 6, 4]), [7, 0, 8])
test_case.assertEqual(add_two_numbers([0], [0]), [0])
test_case.assertEqual(
    add_two_numbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]), [8, 9, 9, 9, 0, 0, 0, 1]
)
