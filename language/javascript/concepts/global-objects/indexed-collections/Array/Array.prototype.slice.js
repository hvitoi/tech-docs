// O(n) -> n = end-start

letters = ["a", "b", "c", "d", "e"];

slice = letters.slice(); // copy everything
slice1 = letters.slice(0, 3); // from index 0 to index 3 (excluding)
slice2 = letters.slice(3); // from index 3
slice3 = letters.slice(0, -1); // from index 0 til last index (excluding)

console.log(slice);
console.log(slice1);
console.log(slice2);
console.log(slice3);

const out = letters.slice(0, -1); // same as letters.pop()
