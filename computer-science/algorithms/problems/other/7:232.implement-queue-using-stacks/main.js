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

class Queue {
  constructor() {
    this.s1 = new Stack();
    this.s2 = new Stack();
  }
  // Getter method to return the data from s1, which is the main stack
  get data() {
    return this.s1.data;
  }
  add(record) {
    // Move all the elements to the 's2' stack. While there are elements left.
    while (this.s1.peek()) {
      this.s2.push(this.s1.pop());
    }

    // Add the element to the 's1' first position
    this.s1.push(record);

    // Bring back the elements from the s2 stack
    while (this.s2.peek()) {
      this.s1.push(this.s2.pop());
    }
  }
  remove() {
    return this.s1.pop();
  }
  peek() {
    return this.s1.peek();
  }
}

// Testing

const test = require('node:test');
const assert = require('node:assert');

test('can add elements to a queue', () => {
  const q = new Queue();
  q.add(1);
});

test('can remove elements from a queue', () => {
  const q = new Queue();
  q.add(1);
  q.remove();
});

test('Order of elements is maintained', () => {
  const q = new Queue();
  q.add(1);
  q.add(2);
  q.add(3);

  assert.strictEqual(q.remove(), 1);
  assert.strictEqual(q.remove(), 2);
  assert.strictEqual(q.remove(), 3);
  assert.strictEqual(q.remove(), undefined);
});

test('peek returns, but does not remove, the first value', () => {
  const q = new Queue();
  q.add(1);
  q.add(2);

  assert.strictEqual(q.peek(), 1);
  assert.strictEqual(q.peek(), 1);
  assert.strictEqual(q.remove(), 1);
  assert.strictEqual(q.remove(), 2);
});
