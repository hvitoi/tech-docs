// --- Directions
//   Print out the n-th entry in the fibonacci series.
//   The fibonacci series is an ordering of numbers where
//   each number is the sum of the preceding two.
//   For example, the sequence
//   [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
//   forms the first ten entries of the fibonacci series.
// --- Example:
//   fib(4) === 3
module.exports = fibonacciIterative;

// Iterative solution - LINEAR RUNTIME
function fibonacciIterative(n) {
  // Initial values
  const fib = [0, 1]; // i=1 and i=2

  // Build all fibonacci values for i < n
  for (let i = 2; i < n; i++) {
    fib.push(fib[i - 1] + fib[i - 2]);
  }

  // Return only the desired position
  return fib[n - 1];
}

// Recursive solution
function fibonacciRecursive(n, fib = [0, 1]) {
  if (fib.length === n) return fib[n - 1]; // Base case
  const new_fib = [...fib, fib[fib.length - 1] + fib[fib.length - 2]]; // sum the last 2 elements
  //fib.push(fib[fib.length - 1] + fib[fib.length - 2]);
  return fibonacciRecursive(n, new_fib);
}

// Recursive solution 2 - EXPONENTIAL RUNTIME
function fibonacciExponential(n) {
  // Return the two first series values
  if (n === 1) return 0;
  if (n === 2) return 1;
  // Calls the function again if this is not the first values
  return fibonacciExponential(n - 1) + fibonacciExponential(n - 2); // must be changed to memoize() to call the fast function
}

// Memoized recursive solution: Saves the result of functions with same arguments
// Next time the function is called with same argument, it doesn't need to be rerun
function memoize(fn) {
  const cache = {};
  // ...args means it don't know what args will come, just take all of them as pass as an array
  return function (...args) {
    if (cache[args]) return cache[args];
    const result = fn.apply(this, args); // Calls the fn with the arguments
    cache[args] = result;
    return result;
  };
}

function fibMemoized(n, mem = {}) {
  // return cached value (if present)
  if (mem[n]) return mem[n];

  // return bottom values
  if (n === 1) mem[n] = 0;
  if (n === 2) mem[n] = 1;

  // recurse (and cache) if not yet on the bottom
  if (n !== 1 && n !== 2) mem[n] = fibMemoized(n - 1) + fibMemoized(n - 2);

  // cache
  return mem[n];
}

// Execution
var start = Date.now();
console.log(fibonacciIterative(30));
var end = Date.now();
console.log(`Execution time: ${end - start} ms`);

var start = Date.now();
console.log(fibonacciRecursive(30));
var end = Date.now();
console.log(`Execution time: ${end - start} ms`);

var start = Date.now();
console.log(fibonacciExponential(30));
var end = Date.now();
console.log(`Execution time: ${end - start} ms`);

var start = Date.now();
console.log(memoize(fibonacciExponential)(30));
var end = Date.now();
console.log(`Execution time: ${end - start} ms`);

var start = Date.now();
console.log(fibMemoized(30));
var end = Date.now();
console.log(`Execution time: ${end - start} ms`);
