/**
 *
 * Clojure is a function that returns another function
 * The "inner function" references a variable declared in the outer "function"
 * The variable of the outer function is maintained in memory even after it has returned and popped out of the callstack
 * Therefore it can be used as a state
 */

/**
 * A Class in JS is actually a different syntax for functions and clojures
 * E.g., a class has a state and inner methods can change the state of the outer function (the class itself)
 */

// Memoized functions store the function itself an a cache object
function memoize(fn) {
  const cache = {};
  // ...args means it doesn't know what args will come, just take all of them as pass as an array (e.g., [2,5])
  return function (...args) {
    // If the result is already cached, show the cached result
    if (cache[args]) {
      console.log("Response found in cache!");
      return cache[args];
    }
    console.log("Response not found in cache!");

    // If there is no cache. calls the fn with the new arguments
    const result = fn.apply(this, args);

    // Saves the result to the cache
    cache[args] = result;

    // Return the calculated value
    return result;
  };
}

const sum = (a, b) => a + b;
const sumMemoized = memoize(sum);

sumMemoized(2, 5);
sumMemoized(2, 5);
