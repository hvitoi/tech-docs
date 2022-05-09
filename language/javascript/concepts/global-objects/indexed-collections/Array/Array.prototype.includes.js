const numbers = [1, 2, 3, 4];
console.log(numbers.includes(5)); // false
console.log(numbers.includes(1, 2)); // contains the element 1 starting from index 2? no!

console.log([1, 2, 3].includes(3, 2)); // true
console.log([19, 21, 46].includes(19, 1)); // false
console.log([19, 21, 46].includes(46, -1)); // true
console.log([1, 2, NaN].includes(NaN)); // true

// ---
const myArr = ["Henrique", "Tercio"];

// Sweep an array and return true
const res = myArr.includes("Henrique");

// ---

// Manually implementing includes
Array.prototype.contains = function (obj) {
  var i = this.length;
  while (i--) {
    if (this[i] === obj) {
      return true;
    }
  }
  return false;
};
