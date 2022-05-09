class Node {
  constructor(data) {
    this.data = data;
    this.left = null;
    this.right = null;
  }
  insert(data) {
    // do not accept duplicate values
    if (data < this.data) {
      if (!this.left) this.left = new Node(data);
      else this.left.insert(data);
    } else if (data > this.data) {
      if (!this.right) this.right = new Node(data);
      else this.right.insert(data);
    }
  }
  contains(value) {
    // True if value is found
    if (value === this.data) return this;

    // Recurse with the node on the left or right
    if (value < this.data && this.left) return this.left.contains(value);
    else if (value > this.data && this.right) return this.right.contains(value);

    // False if all iterations do not match
    return null;
  }
  toArray(arr = []) {
    if (this.left) this.left.toArray(arr);
    arr.push(this.data);
    if (this.right) this.right.toArray(arr);
    return arr;
  }
  validate(
    node = this,
    min = Number.NEGATIVE_INFINITY,
    max = Number.POSITIVE_INFINITY
  ) {
    if (node.data > max) return false;
    if (node.data < min) return false;

    // When going to the left, a new "max" is assigned
    if (node.left && !this.validate(node.left, min, node.data)) {
      return false;
    }

    // When going to the right, a new "min" is assigned
    if (node.right && !this.validate(node.right, node.data, max)) {
      return false;
    }

    return true;
  }
  invert() {
    [this.left, this.right] = [this.right, this.left];
    if (this.left) this.left.invert();
    if (this.right) this.right.invert();
    return this;
  }
}

/**
 * Insert
 */
var n = new Node(10);
n.insert(5);
n.insert(15);
n.insert(0);
n.insert(20);
console.log(n);

/**
 * Validate
 */
var n = new Node(10);
n.insert(5);
n.insert(15);
n.insert(0);
n.insert(20);
console.log(n.validate()); // true

var n = new Node(10);
n.insert(5);
n.insert(15);
n.insert(0);
n.insert(20);
n.left.left.right = new Node(999);
console.log(n.validate()); // false

/**
 * toArray
 */
var n = new Node(10);
n.insert(5);
n.insert(15);
n.insert(0);
n.insert(20);
console.log(n.toArray());

/**
 * Invert
 */
var n = new Node(10);
n.insert(5);
n.insert(15);
n.insert(0);
n.insert(20);
console.log(n.invert());
