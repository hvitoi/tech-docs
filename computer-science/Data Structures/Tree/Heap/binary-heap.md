# Heap

- **Max Heap**
  - A node value will always be greater than its children values
- **Min Heap**
  - A node value will always be smaller than its children values

- <https://www.youtube.com/watch?v=k72DtCnY4MU>

## Implementation from array

- A heap is a `complete binary tree` (has an order for insertion)
- Because it has an order of insertion, it can be `represented as an array`
- To fill a binary heap from an array simply add them from left to right and fill the binary tree top-down, left-right

- **Parent** $i_p = \frac{(i-1)}{2}$
- **Left child** $i_l = 2*i+1$
- **Right child** $i_r = 2*i+2$

## Operations (Binary Heap)

- `Search`: $O(n)$
- `Insert`: $O(log\ n)$ (due to restoration)
- `Remove`: $O(log\ n)$ (due to restoration)
- `Peek`: $O(1)$ (the root node)
