// O(N)
// "Shift" removes an element from the beginning of an array
const arr = [];

arr.unshift(1); // add element to beginning
arr.unshift(2); // add element to beginning
const element = arr.shift(); // get number 2

console.log(element);
console.log(arr);
