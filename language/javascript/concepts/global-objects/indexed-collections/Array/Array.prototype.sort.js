// O(N log N)

const numbers = [2, 5, 1000, 3, 4];
const letters = ["d", "b", "c", "a"];

// Sort numbers in alphabetical order
numbers.sort();
console.log(numbers);

// Sort letters in alphabetical order
letters.sort();
console.log(letters);

// ---

// Sort numbers: ascending order
numbers.sort((a, b) => a - b);
console.log(numbers);

// Sort numbers: descending order
numbers.sort((a, b) => b - a);
console.log(numbers);

// --

// Sort dates
const dates = [
  new Date("2018-01-17T12:00:00.000Z"),
  new Date("2015-01-17T12:00:00.000Z"),
  new Date("2017-01-17T12:00:00.000Z"),
];
dates.sort((a, b) => a - b);
console.log(dates);
