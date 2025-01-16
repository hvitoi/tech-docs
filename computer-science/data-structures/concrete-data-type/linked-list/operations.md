# Operations

## Search

$$O(n)$$

## Access

$$O(n)$$

- To access an element, it has to iterate over each node (starting from the root node) until the desired element is found
- An element at the beginning will be `O(1)` and at the end `O(N)`

## Insert

$$O(n)$$

- To write at a specific index, first the list need to be iterated until the desired position and then change the reference to the next element
- To write an element at the beginning will be `O(1)` and at the end `O(N)`
