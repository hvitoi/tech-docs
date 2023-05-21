// --- Directions
//   Write a function that accepts a positive number N.
//   The function should console log a pyramid shape
//   with N levels using the # character.  Make sure the
//   pyramid has spaces on both the left *and* right hand sides
// --- Examples
//   pyramid(1)
//       '#'
//   pyramid(2)
//       ' # '
//       '###'
//   pyramid(3)
//       '  #  '
//       ' ### '
//       '#####'
module.exports = pyramid1;

function pyramidRecursive(n, levelNumber = 1, levelString = "") {
  if (levelNumber > n) return; // if the final level is reached (base case)

  const width = 2 * n - 1; // always odd
  const hashWidth = 2 * levelNumber - 1; // always odd
  const whiteWidth = width - hashWidth; // always pair

  if (levelString.length === width) {
    console.log(levelString);
    pyramidRecursive(n, levelNumber + 1, "");
  } else {
    levelString =
      levelString.length < whiteWidth / 2 ||
      levelString.length >= whiteWidth / 2 + hashWidth
        ? levelString + " "
        : levelString + "#";
    pyramidRecursive(n, levelNumber, levelString);
  }
}

// Add the white spaces + hashes + white spaces
function pyramid1(n) {
  let width = 1 + 2 * (n - 1); // Calculate the bottom width of the pyramid // (n*2)-1
  for (let level = 1; level <= n; level++) {
    // Reset the stair on each new level

    // Calculate the number of '#' and ' ' for the level
    let h = 1 + 2 * (level - 1);
    let w = width - h;

    // Build each stair
    let stair = "";
    for (let i = 1; i <= w / 2; i++) stair += " "; // build the first half of white spaces
    for (let i = 1; i <= h; i++) stair += "#"; // concat the hashes
    for (let i = 1; i <= w / 2; i++) stair += " "; // concat the last half of white spaces
    //stair = " ".repeat(w / 2) + "#".repeat(h) + " ".repeat(w / 2);

    // Print each level of the pyramid, from top to bottom
    console.log(stair);
  }
}

// Build from each midpoint
function pyramid2(n) {
  // Calculate the midpoint index of the pyramid. Total width will always be an odd number
  const midpoint = Math.floor((2 * n - 1) / 2);

  for (let row = 0; row < n; row++) {
    // Reset the level content
    let level = "";

    // Build each level
    for (let column = 0; column < 2 * n - 1; column++) {
      // Check if the position is in the range of pounds
      if (midpoint - row <= column && midpoint + row >= column) {
        level += "#";
      } else {
        level += " ";
      }
    }

    // Print the level
    console.log(level);
  }
}

// Recursive solution
function pyramid3(n, row = 0, level = "") {
  // If the pyramid is complete...
  if (row === n) return;

  // If the level is complete, print the level
  if (level.length === 2 * n - 1) {
    console.log(level);
    return pyramid3(n, row + 1);
  }

  // If the level is incomplete, build the level
  const midpoint = Math.floor((2 * n - 1) / 2);
  let add;
  // level.length is the current character of the level being built
  if (midpoint - row <= level.length && midpoint + row >= level.length) {
    add = "#";
  } else {
    add = " ";
  }
  pyramid3(n, row, level + add);
}

pyramid1(10);
pyramid2(10);
pyramid3(10);
pyramidRecursive(10);
