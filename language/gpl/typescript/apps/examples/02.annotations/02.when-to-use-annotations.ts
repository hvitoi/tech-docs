// -- WHEN TO USE ANNOTATIONS

// 1- Function that returns the 'any' type
const json = `{"x": 10, "y": 20}`;
const coordinates: { x: number; y: number } = JSON.parse(json); // otherwise would return type 'any'
console.log(coordinates); // TS doesn't know what result would come out from JSON.parse()

// 2- When the variable is declared, but not initialized
let words = ['red', 'green', 'blue'];
let foundWord: boolean; // let foundWord = false;    would be better!
for (let i = 0; i < words.length; i++) {
  if (words[i] === 'green') {
    foundWord = true;
  }
}
foundWord = words.some((e) => e === 'green');

// 3- Varible whose type cannot be inferred correctly
let numbers = [-10, -1, 12];
let numberAboveZero: boolean | number = false; // can be of two types

for (let i = 0; i < numbers.length; i++) {
  if (numbers[i] > 0) {
    numberAboveZero = numbers[i];
  }
}
