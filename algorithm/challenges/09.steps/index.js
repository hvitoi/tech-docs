// --- Directions
//   Write a function that accepts a positive number N.
//   The function should console log a step shape
//   with N levels using the # character.  Make sure the
//   step has spaces on the right hand side!
//   --- Examples
//     steps(2)
//         '# '
//         '##'
//     steps(3)
//         '#  '
//         '## '
//         '###'
//     steps(4)
//         '#   '
//         '##  '
//         '### '
//         '####'
module.exports = steps;

// Building each step with if statements
function steps(n) {
  let step;
  for (let i = 1; i <= n; i++) {
    step = "";
    for (let j = 1; j <= n; j++) {
      if (j <= i) step += "#";
      else step += " ";
    }
    console.log(step);
  }
}

// Repeat
function stepsRepeat(n) {
  for (let i = 1; i <= n; i++) {
    console.log("#".repeat(i) + " ".repeat(n - i));
  }
}

// Repeat
function stepsRepeatRecursive(n, s = 1) {
  if (s > n) return; // if the highest step is reached
  console.log("#".repeat(s) + " ".repeat(n - s));
  stepsRepeatRecursive(n, s + 1);
}

// Recursive solution
function stepsRecursive(n, s = 1) {
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
function stepsRecursiveNoFors(n, row = 0, stair = "") {
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

steps(10);
stepsRecursive(10);
stepsRecursiveNoFors(3);
stepsRepeat(10);
stepsRepeatRecursive(4);
