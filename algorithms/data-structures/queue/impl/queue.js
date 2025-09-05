class Queue {
  constructor() {
    this.data = [];
  }

  add(record) {
    this.data.unshift(record); // Add to the first place
  }

  remove() {
    return this.data.pop(); // Remove from the last place
  }

  get peek() {
    return this.data[this.data.length - 1];
  }
}
