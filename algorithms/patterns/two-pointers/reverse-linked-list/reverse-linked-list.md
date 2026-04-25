# Reverse Linked List

> [LeetCode #206](https://leetcode.com/problems/reverse-linked-list/) — Easy

Given the `head` of a singly linked list, reverse the list, and return the reversed list.

## Examples

### Example 1

```text
Input:  head = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
```

### Example 2

```text
Input:  head = [1, 2]
Output: [2, 1]
```

### Example 3

```text
Input:  head = []
Output: []
```

## Constraints

- The number of nodes in the list is in the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

## Follow-up

A linked list can be reversed either iteratively or recursively. **Could you implement both?**

## What to practise

- Iterative: keep three pointers `prev`, `curr`, `nxt`. At each step save `nxt = curr.next`, rewire `curr.next = prev`, then advance `prev = curr; curr = nxt`. Return `prev`.
- Recursive: reverse the rest of the list, then make `head.next.next = head; head.next = None`.
- Edge: empty list and single-node list both return as-is.
