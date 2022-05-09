// --- Directions
//   Implement a Queue datastructure using two stacks.
//   *Do not* create an array inside of the 'Queue' class.
//   Queue should implement the methods 'add', 'remove', and 'peek'.
//   For a reminder on what each method does, look back
//   at the Queue exercise.
// --- Examples
//   const q = new Queue();
//   q.add(1);
//   q.add(2);
//   q.peek();  // returns 1
//   q.remove(); // returns 1
//   q.remove(); // returns 2

const Stack = require("./stack");

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

const q = new Queue();
q.add(1);
console.log(q.data);

q.add(2);
console.log(q.data);

console.log(q.peek());
console.log(q.data);

q.remove();
console.log(q.data);

q.remove();
console.log(q.data);

module.exports = Queue;
