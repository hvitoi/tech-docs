// --- BUBBLE SORT O(n^2)
//   Look each pair of numbers inside the array (e.g. #1 & #2, #2 & #3, #3 & #4 ... )
//   Check if the left element is greater than the right element
//   If it's greater, elements are swapped
//   After 1st iteration, the last element of the array will be the largest
//   Repeat the process n-1 times (n = array length)

function bubbleSort(arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        const lesser = arr[j + 1];
        arr[j + 1] = arr[j];
        arr[j] = lesser;
      }
    }
  }
  return arr;
}

function bubbleSort2(collection) {
  let { length } = collection; // Destructuring the collection object
  while (length > 1) {
    for (let i = 0; i < length - 1; i++) {
      if (collection[i] > collection[i + 1]) {
        const aux = collection[i + 1];
        collection[i + 1] = collection[i];
        collection[i] = aux;
      }
    }
    length--;
  }
  return collection;
}

module.exports = bubbleSort;

console.log(bubbleSort([10, 3, 2, -1, 0]));
