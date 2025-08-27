class Node {
  constructor(data) {
    this.data = data;
    this.children = [];
  }
  add(data) {
    this.children.push(new Node(data));
  }
  remove(data) {
    // Removes every node that matches the data
    this.children = this.children.filter((child) => {
      return child.data !== data;
    });
  }
}

// A tree has a 'root' property, which is the node at the top
class Tree {
  constructor() {
    this.root = null;
  }
  // Traverse by "breadth first" (broad)
  traverseBF(fn) {
    const nodes = [this.root];
    // Iterates while there is any value inside of the array
    while (nodes.length) {
      const node = nodes.shift(); // Take the first and remove
      fn(node); // Run the current node
      nodes.push(...node.children); // Push its children to the end
      // Spread operator! Split the elements of the array
    }
  }
  // Traverse by "depth first" (deep)
  traverseDF(fn) {
    const nodes = [this.root];
    while (nodes.length) {
      const node = nodes.shift(); // Take the first and remove
      fn(node); // Run the current node
      nodes.unshift(...node.children); // Push its children to the start
    }
  }
  traverseDF_recursive(fn, node = this.root) {
    fn(node);
    const num_children = node.children.length;
    if (!num_children) return; // Base case
    for (let i = 0; i < num_children; i++) {
      this.traverseDF_recursive(fn, node.children[i]);
    }
  }

  traverseDF_recursive2(fn, nodes = [this.root]) {
    if (nodes.length === 0) return;
    for (let node of nodes) {
      fn(node);
      traverseDF_recursive2(node.children);
    }
  }
}

const letters = [];
const t = new Tree();
t.root = new Node("a");
t.root.add("b");
t.root.add("c");
t.root.children[0].add("d");

t.traverseBF((node) => {
  letters.push(node.data);
});

/**
 * Traverse array
 */

const myNode = [[[[1], [2]], [3]], [4], [5]];

const arrTraverseDF = (node) => {
  if (!Array.isArray(node)) {
    console.log(node);
    return; // base case
  }
  node.forEach((el) => {
    arrTraverseDF(el);
  });
};

const arrTraverseBF = (node) => {
  // if (node.length === 0) return; // base case

  const nextLevel = [];
  node.forEach((el) => {
    if (!Array.isArray(el)) {
      console.log(el);
    } else {
      nextLevel.push(...el);
    }
  });

  if (nextLevel.length !== 0) {
    return arrTraverseBF(nextLevel); // base case
  }
};

// arrTraverseDF(myNode);
arrTraverseBF(myNode);
