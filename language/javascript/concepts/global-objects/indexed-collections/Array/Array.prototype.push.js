// O(1)
// Push element to the end of an array
const arr = [];

arr.push(1); // returns the index (0)
arr.push(2); // returns the index (1)
arr.push(3, 4); // push multiple elements
arr.push(...[5, 6]); // push multiple elements in an array

console.log(arr);
