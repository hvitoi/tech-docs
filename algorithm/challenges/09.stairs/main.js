// Building each step with if statements
function stairs(n) {
  let stairs = []
  let step;
  for (let i = 1; i <= n; i++) {
    step = "";
    for (let j = 1; j <= n; j++) {
      if (j <= i) step += "#";
      else step += " ";
    }
    stairs.push(step)
  }
  return stairs;
}

// Repeat
function stairsRepeat(n) {
  for (let i = 1; i <= n; i++) {
    console.log("#".repeat(i) + " ".repeat(n - i));
  }
}

// Repeat
function stairsRepeatRecursive(n, s = 1) {
  if (s > n) return; // if the highest step is reached
  console.log("#".repeat(s) + " ".repeat(n - s));
  stairsRepeatRecursive(n, s + 1);
}

// Recursive solution
function stairsRecursive(n, s = 1) {
  // Leave the solution if the last step is reached
  if (s === n + 1) return; // Base case

  // Build the step conditionally
  let step = "";
  for (let i = 1; i <= n; i++) {
    if (i <= s) step += "#";
    else step += " ";
  }
  // Log the step
  console.log(step);
  steps2(n, s + 1);
}

// Recursive solution without fors
function stairsRecursiveNoFors(n, row = 0, stair = "") {
  // Leave the solution if the step limit is reached
  if (n === row) return;

  // Build the stair
  if (n !== stair.length) {
    const add = stair.length <= row ? "#" : " ";
    return steps3(n, row, stair + add);
  }

  // Print the stair if it is completed
  else {
    console.log(stair);
    return steps3(n, row + 1); // no stair is provided (start empty stair)
  }
}

// Testing

const test = require('node:test');
const assert = require('node:assert');

test('build stairs ', () => {
  assert.deepStrictEqual(stairs(1), ['#'])
  assert.deepStrictEqual(stairs(2), ['# ', '##'])
  assert.deepStrictEqual(stairs(3), ['#  ', '## ', '###'])
});
