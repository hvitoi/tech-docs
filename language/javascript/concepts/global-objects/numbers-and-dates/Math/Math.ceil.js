const number1 = 1.23;
const number2 = 1.5;
const number3 = 1.9;
const number4 = 1;

console.log(Math.ceil(number1));
console.log(Math.ceil(number2));
console.log(Math.ceil(number3));
console.log(Math.ceil(number4));

// ---

const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const middleIndex = Math.floor(arr.length / 2);
const left = arr.slice(0, middleIndex);
const right = arr.slice(middleIndex);
console.log(middleIndex, left, right);
