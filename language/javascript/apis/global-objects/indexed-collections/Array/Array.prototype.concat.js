// O(N+M)

// Array gets copied with additional element
// Similar to "push", but returns the whole array (instead of the pushed element)
const arr1 = ["A", "B", "C"];
const arr2 = ["D", "E"];
const arr3 = "F";

console.log(arr1.concat(arr2).concat(arr3));
console.log(arr1); // does not change the original array
