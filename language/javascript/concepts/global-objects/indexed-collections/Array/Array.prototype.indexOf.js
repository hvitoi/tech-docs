// O(N)

letters = ["a", "b", "c", "d", "e", "b"];

index = letters.indexOf("b"); // returns 1, which is the first index of "b"
index2 = letters.indexOf("f"); // Returns -1, because there is no occurrence
index3 = letters.indexOf("c", 2); // Starts the search from index 2

console.log(index);
console.log(index2);
console.log(index3);

//

let arr = ["Krunal", "Ankit", "Rushabh"];
let arrContainString = arr.indexOf("Krunal") > -1;
console.log(arrContainString);
