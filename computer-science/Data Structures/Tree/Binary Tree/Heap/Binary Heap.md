# Heap

- **Max Heap**
  - A node value will always be greater than its children values
- **Min Heap**
  - A node value will always be smaller than its children values

- A head is always a `complete binary tree`
- That means it has an order of elements and it can be implemented on top of arrays

## Restoration

- On every insertion/removal, the heap has to be restored in order to "restore" its datastructure properties (max/min order)

- `Restoration on insertion`
  - Bubble the item upwards, by comparing it with the parent nodes

- `Restoration on removal`
  - The last item in the complete tree takes place in the removed items
  - Bubble the item downwards, by comparing it with the child nodes

## Operations (Binary Heap)

- `Search`: $O(n)$
- `Insert`: $O(log\ n)$ (due to restoration)
- `Remove`: $O(log\ n)$ (due to restoration)
- `Peek`: $O(1)$ (the root node)
