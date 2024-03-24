# Linked List

- Elements are not stored in contiguous addresses on the memory
- **Pros**
  - No need to `pre-allocate` spaces (it's saved randomly in memory)
  - Insertion does not need to shift the remaining elements

## Node

- A node contains two information
  - `value`: the actual data of an element
  - `next`: reference (memory address) to the next element in the list
- `Head Node`: the first node of the list
- `Last Node`: the last node of the list (does not contain a next element)

## Access

- To access an element, it has to iterate over each node (starting from the root node) until the desired element is found
- Access at the end: `O(N)` (worst case)
- Access at the beginning: `O(1)`

## Write

- To write at a specific index, first the list need to be iterated until the desired position and then change the reference to the next element
- Write at the end `O(N)` (worst case)
- Write at the beginning `O(1)`
