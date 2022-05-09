// fill index 1 and 2 with "9"
const arr = [1, 2, 3, 4, 5];
const filledArr = arr.fill(9, 1, 3);
console.log(filledArr);

// ---
// fill index 1 onwards with "9"
const arr2 = [1, 2, 3, 4, 5];
const filledArr2 = arr2.fill(9, 1);
console.log(filledArr2);

// ---
// fill everything with "0"
const arr3 = [1, 2, 3, 4, 5];
const filledArr3 = arr3.fill(0);
console.log(filledArr3);
