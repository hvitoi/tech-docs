// --- Directions
//   1) Complete the task in weave/queue.js
//   2) Implement the 'weave' function.  Weave
//   receives two queues as arguments and combines the
//   contents of each into a new, third queue.
//   The third queue should contain the *alterating* content
//   of the two queues.  The function should handle
//   queues of different lengths without inserting
//   'undefined' into the new one.
//   *Do not* access the array inside of any queue, only
//   use the 'add', 'remove', and 'peek' functions.
// --- Example
//   const queueOne = new Queue();
//   queueOne.add(1);
//   queueOne.add(2);
//   const queueTwo = new Queue();
//   queueTwo.add('Hi');
//   queueTwo.add('There');
//   const q = weave(queueOne, queueTwo);
//   q.remove() // 1
//   q.remove() // 'Hi'
//   q.remove() // 2
//   q.remove() // 'There'
module.exports = weave;

const Queue = require("./queue");

function weave(q1, q2) {
  const queue = new Queue();

  while (q1.peek || q2.peek) {
    if (q1.peek) queue.add(q1.remove());
    if (q2.peek) queue.add(q2.remove());
  }
  return queue;
}

const q1 = new Queue();
q1.add(1);
q1.add(2);

const q2 = new Queue();
q2.add("Hi");
q2.add("There");

const q = weave(q1, q2);
console.log(q.data);
