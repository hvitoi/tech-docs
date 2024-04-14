# Linked List

- Elements are not stored in contiguous addresses on the memory
- **Pros**
  - No need to `pre-allocate` spaces (it's saved randomly in memory)
  - Insertion does not need to shift the remaining elements (like it is done in Arrays)
- **Cons**
  - Compared to Arrays, the traversal is slower, given that the sequential read is much more efficient (with caching systems)
- Linked Lists are good for `manipulating elements in the beginning` (while Arrays are good for `manipulating elements in the ending`)

## Node

- A linked list is composed of `Nodes`, which is represented by:
  - **value**: the actual data of an element
  - **next**: reference (memory address) to the next element in the list
- `Head Node`: the first node of the list, no other node points to it
- `Tail Node`: the last node of the list, does not point to anything (this is stored only in Doubly Linked Lists)

## Access

- To access an element, it has to iterate over each node (starting from the root node) until the desired element is found
- Access at the beginning: `O(1)`
- Access at the end: `O(N)`

## Write

- To write at a specific index, first the list need to be iterated until the desired position and then change the reference to the next element
- Write at the beginning `O(1)`
- Write at the end `O(N)`

## Singly Linked List

- A node has **data** and **next**
- The Linked List has a **head** node

## Doubly Linked List

- Similar to a Singly Linked List, but also stores the `previous node`
- A node has **data**, **next** and **prev**
- Allows traversing the list backwards
- The Linked List has a **head** and a **tail**
- **Pros**
  - The search can be more efficient, because depending on the target index, we can start backwards
- **Cons**
  - Each node consumes more memory, because it has to store the prev node
