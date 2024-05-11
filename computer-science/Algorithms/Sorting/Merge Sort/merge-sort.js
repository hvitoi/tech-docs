function mergeSort2(arr) {
  if (arr.length === 1) return arr; // Base case

  // Slice the array in a half
  const middleIndex = Math.floor(arr.length / 2);
  const left = arr.slice(0, middleIndex);
  const right = arr.slice(middleIndex);

  // Merge two sorted arrays
  return mergedSorted(mergeSort2(left), mergeSort2(right));
}
function mergedSorted(left, right) {
  const mergedArr = []; // Array with the merged left and right

  // While there is left or right
  while (left.length && right.length) {
    if (left[0] < right[0]) mergedArr.push(left.shift());
    else mergedArr.push(right.shift());
  }

  // Return the result with remainder arrays (either left or right will have a remainder)
  return [...mergedArr, ...left, ...right];
}
// console.log(mergeSort2([10, 3, 2, -1, 0]));

// ---------

const mergeSort = (arr) => {
  if (arr.length <= 1) return arr;

  const midIndex = Math.floor(arr.length / 2);
  const left = arr.slice(0, midIndex);
  const right = arr.slice(midIndex);

  return sortAndMerge(mergeSort(left), mergeSort(right));
};

const sortAndMerge = (left, right) => {
  return left[0] < right[0] ? [...left, ...right] : [...right, ...left];
};

console.log(mergeSort([10, 3, 2, -1, 0]));
