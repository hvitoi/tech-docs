# Array List

- Stores items `contiguously in the memory`
  - The `physical order` (memory) is the same as the `logical order` (viewed by the user)
- Each item has an `index` which is sequential (starting from 0)

## Static Array (Array)

- The size of the array is fixed. Cannot be resized

## Dynamic Array (Vector)

- The size of the array adjusts dynamically based on the current number of items
- Under the hood the array is copied over to a new location if it needs more memory (more elements than its size)
- On dynamic arrays, an insert operation can be $O(n)$ if the array needs to be resized
