// --- Directions
//   Given the root node of a tree, return
//   an array where each element is the width
//   of the tree at each level.
// --- Example
//   Given:
//       0
//     / |  \
//   1   2   3
//   |       |
//   4       5
//   Answer: [1, 3, 2]

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

module.exports = levelWidth;
