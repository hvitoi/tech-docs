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

  // new 'peek' method looks the next element to be removed
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

// const q1 = new Queue();
// q1.add(1);
// q1.add(2);

// const q2 = new Queue();
// q2.add("Hi");
// q2.add("There");

// const q = weave(q1, q2);
// console.log(q.data);

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
