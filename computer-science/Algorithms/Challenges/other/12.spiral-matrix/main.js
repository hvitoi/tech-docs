// 4 directions
function matrix1(n) {
  // Initialize matrix with Zeroes
  const mat = [];
  for (let i = 0; i < n; i++) {
    const row = [];
    for (let j = 0; j < n; j++) {
      row.push(0);
    }
    mat.push(row);
  }

  // Initial values
  let direction = "right"; // Possible directions: right, down, left, up
  let row = 0;
  let col = 0;

  // Write matrix
  for (let i = 1; i <= n * n; i++) {
    debugger;
    switch (direction) {
      case "right":
        mat[row][col] = i;
        if (mat[row][col + 1] === 0) col++;
        else {
          direction = "down";
          row++;
        }
        break;
      case "down":
        mat[row][col] = i;
        if (mat[row + 1]) {
          if (mat[row + 1][col] === 0) row++;
          else {
            direction = "left";
            col--;
          }
        } else {
          direction = "left";
          col--;
        }
        break;
      case "left":
        mat[row][col] = i;
        if (mat[row][col - 1] === 0) col--;
        else {
          direction = "up"; // If not, change direction
          row--;
        }
        break;
      case "up":
        mat[row][col] = i;
        if (mat[row - 1]) {
          if (mat[row - 1][col] === 0) row--;
          else {
            direction = "right";
            col++;
          }
        } else {
          direction = "right";
          col++;
        }
        break;
    }
  }
  return mat;
}

// Divide the matrix in 4 lines
function matrix2(n) {
  const results = [];

  // Create an array for each row
  for (let i = 0; i < n; i++) {
    results.push([]);
  }

  let counter = 1;
  let startColumn = 0;
  let endColumn = n - 1;
  let startRow = 0;
  let endRow = n - 1;
  while (startColumn <= endColumn && startRow <= endRow) {
    // Top row
    for (let i = startColumn; i <= endColumn; i++) {
      results[startRow][i] = counter;
      counter++;
    }
    startRow++;

    // Right column
    for (let i = startRow; i <= endRow; i++) {
      results[i][endColumn] = counter;
      counter++;
    }
    endColumn--;

    // Bottom row
    for (let i = endColumn; i >= startColumn; i--) {
      results[endRow][i] = counter;
      counter++;
    }
    endRow--;

    // Left column
    for (let i = endRow; i >= startRow; i--) {
      results[i][startColumn] = counter;
      counter++;
    }
    startColumn++;
  }

  return results;
}

// Testing

const test = require('node:test');
const assert = require('node:assert');

test('matrix produces a 2x2 array', () => {
  assert.deepStrictEqual(matrix1(2),
    [[1, 2],
    [4, 3]]);
});

test('matrix produces a 3x3 array', () => {
  assert.deepStrictEqual(matrix1(3),
    [[1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]]);
});

test('matrix produces a 4x4 array', () => {
  assert.deepStrictEqual(matrix1(4),
    [[1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]]);
});
