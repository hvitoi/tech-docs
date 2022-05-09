const set = new Set(["b", "c", "a"]);
console.log(set); // Set(3) { 'b', 'c', 'a' }
console.log(...set); // b c a

//

// Use to remove duplicate elements from the array
const numbers = [2, 3, 4, 4, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 5, 32, 3, 4, 5];
console.log([...new Set(numbers)]);
// [2, 3, 4, 5, 6, 7, 32]
