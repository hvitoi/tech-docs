class Node {
  constructor(data, next = null) {
    this.data = data;
    this.next = next;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
  }

  size() {
    let node = this.head;
    let size = 0;
    while (node) {
      size++;
      node = node.next;
    }
    return size;
  }
  clear() {
    this.head = null;
  }
  getAt(index) {
    // Check if index is valid
    if (index >= this.size() || index < 0) return null;

    let node = this.head;

    // Go to the node of index 'index'
    for (let i = 0; i < index; i++) {
      node = node.next;
    }
    return node;
  }
  removeAt(index) {
    // Check there is a node for the index 'index'
    if (!this.getAt(index)) return null;

    // Handle case the node is the first
    if (index === 0) {
      this.head = this.getAt(index + 1) || null;
      return;
    }

    // Skip the Node of index 'index'
    this.getAt(index - 1).next = this.getAt(index + 1) || null; // if there is no next element then null
  }
  insertAt(data, index) {
    // Insert node at index <=0
    if (index <= 0) {
      this.head = new Node(data, this.head);
      return;
    }
    // Insert node at index >= size
    if (index >= this.size()) {
      this.getAt(this.size() - 1).next = new Node(data);
      return;
    }
    // Insert node inside of bounds
    this.getAt(index - 1).next = new Node(data, this.getAt(index));
  }
  // ************************************* Passing a function as an argument!
  forEach(fn) {
    let node = this.head;
    let index = 0;
    while (node) {
      fn(node, index);
      node = node.next;
      index++;
    }
  }
  // ********************************** Setup a generator function for a loop
  // Allows the list to be iterated with a for-of loop
  *[Symbol.iterator]() {
    let node = this.head;
    while (node) {
      yield node;
      node = node.next;
    }
  }
}

const linkedList = new LinkedList();
linkedList.insertAt("a", linkedList.size());
linkedList.insertAt("b", linkedList.size());
linkedList.insertAt("c", linkedList.size());

linkedList.forEach((el) => console.log(el));
