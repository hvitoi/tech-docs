# Queue

- **FIFO**: First In, First Out
- Ideally built on top of `Linked Lists`
  - If the linked list implementation holds the `tail`, the dequeue would be $O(1)$, otherwise $O(n)$

## Operations

- `Enqueue`: add element to the end of the queue
- `Dequeue`: remove the first element from the beginning of the queue
- `Peek`: return the first element in the beginning of the queue without removing it

## Code example

```javascript
class Queue {
  constructor() {
    this.data = [];
  }

  add(record) {
    this.data.unshift(record); // Add to the first place
  }

  remove() {
    return this.data.pop(); // Remove from the last place
  }
}
```
