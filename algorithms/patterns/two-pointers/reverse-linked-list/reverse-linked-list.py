# https://leetcode.com/problems/reverse-linked-list/ - 24 k likes Apr-2026
# %%
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    val: int
    next: Node | None = None


def to_list(head: Node | None) -> list[int]:
    acc = []
    while head:
        acc.append(head.val)
        head = head.next
    return acc


def from_list(values: list[int]) -> Node | None:
    head: Node | None = None
    for v in reversed(values):
        head = Node(v, head)
    return head


# %%
def reverse_iterative(head: Node | None) -> Node | None:
    """
    Three-pointer walk: at each step stash `next`, flip `curr.next` to point
    backward, then advance.

    Time:  O(n)
    Space: O(1)
    """
    prev: Node | None = None
    curr = head

    while curr:
        nxt = curr.next  # stash before we overwrite
        curr.next = prev  # flip the link
        prev = curr  # advance window
        curr = nxt

    return prev  # prev is the new head once curr falls off the end


# %%
def reverse_recursive(head: Node | None) -> Node | None:
    """
    Recurse to the tail, then on the way back flip each link:
    `head.next.next = head` makes the next node point back at us;
    `head.next = None` severs the old forward link (becomes the new tail).

    Time:  O(n)
    Space: O(n) call stack
    """
    if head is None or head.next is None:
        return head  # base case: empty or single node — already reversed

    new_head = reverse_recursive(head.next)
    head.next.next = head  # the node ahead of us now points back at us
    head.next = None  # we are the new tail (until our caller fixes it up)
    return new_head


# %%
for fn in (reverse_iterative, reverse_recursive):
    assert to_list(fn(from_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert to_list(fn(from_list([1, 2]))) == [2, 1]
    assert to_list(fn(from_list([1]))) == [1]
    assert to_list(fn(from_list([]))) == []
