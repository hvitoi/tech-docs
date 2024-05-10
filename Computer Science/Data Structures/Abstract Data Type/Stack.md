# Stack

- **LIFO**: Last In, First Out
- Ideally built on top of `Linked Lists`
  - Preferred since it has dynamic memory allocation and sequential read or traversal is not needed

## Operations

- `Push`: add a new element to the top
- `Pop`: remove and return the element from the top
- `Peek`: return the element from the top, but do not remove it

## Code example

```javascript
class Stack {
  constructor() {
    this.data = [];
  }

  push(record) {
    this.data.push(record);
  }

  pop() {
    return this.data.pop();
  }

  peek() {
    return this.data[this.data.length - 1];
  }
}

const stack = new Stack();
stack.push("a");
stack.push("b");
stack.push("c");

console.log(stack.data);

stack.pop();

console.log(stack.data);
```
