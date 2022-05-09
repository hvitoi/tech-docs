/*
 * Complete the 'flippingMatrix' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY matrix as parameter.
 */

function flippingMatrix(matrix) {
  const n = matrix.length;

  // put all elements of the matrix in an array
  const arr = [];
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      arr.push(matrix[i][j]);
    }
  }

  // take the biggest elements of the matrix
  const biggest = arr
    .map((el) => parseInt(el))
    .sort((a, b) => a - b)
    .slice((n / 2) ** 2 * -1);

  // iterate over tje biggest values in the matrix that fit in the quadrant
  for (const big of biggest) {
    matrix = findAndRevert(big, matrix);
  }

  return matrix;
}

const findAndRevert = (num, mat) => {
  const n = mat.length;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (mat[i][j] === num && (i >= n / 2 || j >= n / 2)) {
        // revert column
        if (i >= n / 2) {
          const newMat = mat;
          for (let k = 0; k < n; k++) {
            newMat[k][j] = mat[n - k - 1][j];
          }
          mat = newMat;
        }
        // revert row
        if (j >= n / 2) {
          const newMat = mat;
          for (let k = 0; k < n; k++) {
            newMat[i][k] = mat[i][n - k - 1];
          }
          mat = newMat;
        }
        return mat;
      }
    }
  }
  return mat;
};

console.log(
  flippingMatrix([
    [112, 42, 83, 119],
    [56, 125, 56, 49],
    [15, 78, 101, 43],
    [62, 98, 114, 108],
  ])
);
