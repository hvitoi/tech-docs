// O(N)

const arr = [1, 2, 3, 4, 5];

// Execute instructions for each element in the array
// Cannot use a 'break' inside of a forEach
arr.forEach((element, index, array) => {
  console.log(element); // Element in the array
  console.log(index); // Index of that element
  console.log(array); // Whole array
  arr[index] = 0; // modify the array
});

console.log(arr);
