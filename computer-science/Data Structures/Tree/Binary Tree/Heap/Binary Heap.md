# Heap

- **Max Heap**
  - A node value will always be greater than its children values
- **Min Heap**
  - A node value will always be smaller than its children values

## Restoration

- On every insertion/removal, the heap has to be restored in order to "restore" its datastructure properties (max/min order)

- `Restoration on insertion`
  - Check upward nodes

- `Restoration on removal`
  - Check downward nodes

## Operations (Binary Heap)

- `Search`: $O(n)$
- `Insert`: $O(log\ n)$
- `Remove`: $O(log\ n)$
