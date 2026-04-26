# Queue

- **FIFO**: First In, First Out
- Ideally built on top of `Linked Lists`
  - If the linked list implementation holds the `tail`, the dequeue would be $O(1)$, otherwise $O(n)$

## Operations

- `Enqueue`: $O(1)$ add element to the end of the queue
- `Dequeue`: $O(1)$ remove the first element from the beginning of the queue
- `Peek`: $O(1)$ return the first element in the beginning of the queue without removing it
- `Seach`: $O(n)$

## Implementations

- `Doubly Linked List` - NOT singly (the tail is necessary)
- The "deque" abstract data type also offers the same set of operations that a queue needs

### Python

- queue.Queue
- collections.deque

### C++

- std::queue
- std::deque
