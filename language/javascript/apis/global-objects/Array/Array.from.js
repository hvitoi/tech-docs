//=> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Array.from(Array(10).keys());

//=> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
const arr = [...Array(10).keys()];

//=> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Array.from({ length: 10 }, (_, i) => i + 1);

// ---
const arrFromArray = Array.from([1, 2, 3]);
const arrFromSet = Array.from(new Set([1, 2, 3]));
const arrFromString = Array.from("foo");

console.log(arrFromSet);
console.log(arrFromArray);
console.log(arrFromString);
