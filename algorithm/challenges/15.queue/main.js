class Queue {
  constructor() {
    this.data = [];
  }

  add(record) {
    this.data.unshift(record);
  }

  remove() {
    return this.data.pop();
  }

  get peek() {
    return this.data[this.data.length - 1];
  }
}

// Testing

const test = require('node:test');
const assert = require('node:assert');

test('Queue class', () => {
  const q = new Queue();
  q.add(1);
  q.add(2);

  assert.strictEqual(q.peek, 1);
  assert.strictEqual(q.peek, 1);
  assert.strictEqual(q.remove(), 1);
  assert.strictEqual(q.remove(), 2);
});
