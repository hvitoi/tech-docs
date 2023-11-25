// O(N)

const numbers = [7, 12, 24, 1];
const isEven = (n) => n % 2 === 0;

// Keeps only the elements that return true. Original array is not modified
const evenNumbers = numbers.filter(isEven);
console.log(evenNumbers);
