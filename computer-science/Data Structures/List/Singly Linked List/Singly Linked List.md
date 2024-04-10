# Linked List

- Elements are not stored in contiguous addresses on the memory
- **Pros**
  - No need to `pre-allocate` spaces (it's saved randomly in memory)
  - Insertion does not need to shift the remaining elements

## Node

- A linked list is composed of `Nodes`, which is represented by:
  - **value**: the actual data of an element
  - **next**: reference (memory address) to the next element in the list
- `Head Node`: the first node of the list, no other node points to it
- `Last Node`: the last node of the list, does not point to anything

## Access

- To access an element, it has to iterate over each node (starting from the root node) until the desired element is found
- Access at the beginning: `O(1)`
- Access at the end: `O(N)`

## Write

- To write at a specific index, first the list need to be iterated until the desired position and then change the reference to the next element
- Write at the beginning `O(1)`
- Write at the end `O(N)`
