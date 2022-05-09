/**
 * Generators are functions that can be exited and later re-entered.
 * Their context (variable bindings) will be saved across re-entrances.
 * Arrow-functions cannot be used as generators!
 */

function* myGenerator(i) {
  yield i; // 1st iteration
  yield i + 10; // 2nd iteration
  yield i + 20; // 3rd iteration
}
const gen = myGenerator(10); // initialize generator with i = 10
console.log(gen.next()); // { value: 10, done: false }
console.log(gen.next()); // { value: 20, done: false }
console.log(gen.next()); // { value: 30, done: false }
console.log(gen.next()); // { value: undefined, done: true }

// ---

function* list() {
  yield 1;
  yield 2;
  yield 3;
}
var generator = list();

// Saves the yields into an array
var values = [];
for (let value of generator) {
  values.push(value);
}
console.log(values);

// ---------------------------------

function* numbers() {
  yield 1;
  yield 2;
  yield* moreNumbers(); // Nested generator
  yield 6;
  yield 7;
}

function* moreNumbers() {
  yield 3;
  yield 4;
  yield 5;
}

var generator = numbers();

var values = [];
for (let value of generator) {
  values.push(value);
}
console.log(values);

// ---------------------------------
// GENERATOR AS A METHOD (PROPERTY) IN A CLASS

class Tree {
  constructor(value = null, children = []) {
    this.value = value;
    this.children = children;
  }
  *printValues() {
    // First yield the node's value
    yield this.value;
    // On next(), yield the values of each child
    for (let child of this.children) {
      yield* child.printValues();
    }
  }
}
var tree = new Tree(1, [new Tree(2, [new Tree(4)]), new Tree(3)]);
var values = [];
for (let value of tree.printValues()) {
  values.push(value);
}
console.log(values);

// ----------
// Iterator is a generator function with a key of iterator [Symbol.iterator]

class LinkedList {
  constructor() {
    this.head = null;
  }
  forEach(fn) {
    let node = this.head;
    let index = 0;
    while (node) {
      fn(node, index);
      node = node.next;
      index++;
    }
  }
  // Setup a generator function for a loop
  // Allows the list to be iterated with a for-of loop
  *[Symbol.iterator]() {
    let node = this.head;
    while (node) {
      yield node;
      node = node.next;
    }
  }
}
