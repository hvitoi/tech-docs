export default class Stack {
  constructor() {
    this.top = -1;
    this.items = {};
  }

  push(value) {
    this.top += 1;
    this.items[this.top] = value;
  }

  pop() {
    this.top -= 1;
    return this.items[this.top + 1];
  }

  get peek() {
    return this.items[this.top];
  }
}
