// Replace previous color (prevC) at (x,y) and all surrounding pixels to new color color (newC)

var M = 8;
var N = 8;

function floodFillUtil(screen, x, y, prevC, newC) {
  // Base cases
  if (x < 0 || x >= M || y < 0 || y >= N) return; // out of matrix bounds
  if (screen[x][y] != prevC) return; // color not to be changed

  // Replace the color at (x, y)
  screen[x][y] = newC;

  // Recur for north, east, south and west
  floodFillUtil(screen, x + 1, y, prevC, newC);
  floodFillUtil(screen, x - 1, y, prevC, newC);
  floodFillUtil(screen, x, y + 1, prevC, newC);
  floodFillUtil(screen, x, y - 1, prevC, newC);
}

// It mainly finds the previous color
// on (x, y) and calls floodFillUtil()
function floodFill(screen, x, y, newC) {
  var prevC = screen[x][y];
  if (prevC == newC) return;
  floodFillUtil(screen, x, y, prevC, newC);
}

// Driver code
var screen = [
  [1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 0, 0],
  [1, 0, 0, 1, 1, 0, 1, 1],
  [1, 2, 2, 2, 2, 0, 1, 0],
  [1, 1, 1, 2, 2, 0, 1, 0],
  [1, 1, 1, 2, 2, 2, 2, 0],
  [1, 1, 1, 1, 1, 2, 1, 1],
  [1, 1, 1, 1, 1, 2, 2, 1],
];
var x = 4,
  y = 4,
  newC = 3;
floodFill(screen, x, y, newC);

console.log(screen);
for (let row of screen) {
  console.log(row.join(" "));
}
