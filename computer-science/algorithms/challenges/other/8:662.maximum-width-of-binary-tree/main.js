class Node {
  constructor(data) {
    this.data = data;
    this.children = [];
  }

  add(data) {
    this.children.push(new Node(data));
  }
};

function levelWidth(root) {
  const tree = [[root]];
  let level = 0;
  while (tree[level]) {
    // Start a new level
    const new_level = [];

    // Push the children of all nodes to the next level
    tree[level].forEach((node) => new_level.push(...node.children));

    // Append the new level to the tree if it's not empty
    if (new_level.length) tree.push(new_level);

    // Move to next level
    level++;
  }
  // Extract the size of each level and return
  return tree.map((level) => level.length);
}

function levelWidth2(root) {
  const arr = [root, "s"]; // 's' indicates the start of a new level
  const counters = [0];

  while (arr.length > 1) {
    const node = arr.shift();

    if (node === "s") {
      counters.push(0);
      arr.push("s");
    } else {
      arr.push(...node.children);
      counters[counters.length - 1]++;
    }
  }

  return counters;
}

// Testing

const test = require('node:test');
const assert = require('node:assert');

test('levelWidth returns number of nodes at widest point', () => {
  const root = new Node(0);
  root.add(1);
  root.add(2);
  root.add(3);
  root.children[0].add(4);
  root.children[2].add(5);

  assert.deepStrictEqual(levelWidth(root), [1, 3, 2])
});

test('levelWidth returns number of nodes at widest point', () => {
  const root = new Node(0);
  root.add(1);
  root.children[0].add(2);
  root.children[0].add(3);
  root.children[0].children[0].add(4);

  assert.deepStrictEqual(levelWidth(root), [1, 1, 2, 1])
});
