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
