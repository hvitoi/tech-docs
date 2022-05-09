// Call a function with an array of arguments
const myFn = (text) => {
  console.log(text);
};
myFn.apply(this, ["oi", "haha"]); // 1st arg: oi, 2nd arg: haha (not used by the function)
myFn.apply(null, ["oi", "haha"]); // first arg refers to the desired "this" context -- can be null

// -- memoize
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
