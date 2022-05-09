// 100-sized-array with empty values
var arrEmpty = new Array(100); // [empty, empty, ... , empty]

// 100-sized-array filled with "0" values
const arrZeroes = new Array(100).fill(0); //[0,0, ... , 0]

// loop
new Array(10).fill(0).forEach(() => console.log("hello"));

/**
 * Array destructuring
 */
var [x, y, , z] = [1, 2, 3, 4]; // z=1 , x=2, y=4
console.log(x, y, z);

[x, y] = [y, x]; // x=2, y=1
console.log(x, y);
