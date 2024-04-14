# Queue

- **FIFO**: First In, First Out
- Ideally built on top of `Linked Lists`
  - If the queue implementation holds the `tail`, the dequeue would be $O(1)$, otherwise $O(n)$

## Interface

- `Enqueue`: add element to the end of the queue
- `Dequeue`: remove the first element from the beginning of the queue
- `Peek`: return the first element in the beginning of the queue without removing it
