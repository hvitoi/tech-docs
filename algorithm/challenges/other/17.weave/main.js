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

function weave(q1, q2) {
  const queue = new Queue();

  while (q1.peek || q2.peek) {
    if (q1.peek) queue.add(q1.remove());
    if (q2.peek) queue.add(q2.remove());
  }
  return queue;
}

// Testing

const test = require('node:test');
const assert = require('node:assert');

test('Weave function can combine two queues', () => {
  const one = new Queue();
  one.add(1);
  one.add(2);
  one.add(3);
  one.add(4);

  const two = new Queue();
  two.add('one');
  two.add('two');
  two.add('three');
  two.add('four');

  const result = weave(one, two);

  assert.strictEqual(result.remove(), 1);
  assert.strictEqual(result.remove(), 'one');
  assert.strictEqual(result.remove(), 2);
  assert.strictEqual(result.remove(), 'two');
  assert.strictEqual(result.remove(), 3);
  assert.strictEqual(result.remove(), 'three');
  assert.strictEqual(result.remove(), 4);
  assert.strictEqual(result.remove(), 'four');
  assert.strictEqual(result.remove(), undefined);
});
