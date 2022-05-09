// --- SELECTION SORT O(n^2)
//   Iterates over the whole array n times (n is the length of the array)
//   On each iteration pull the lowest value to the beginning of the array

function selectionSort(arr) {
  for (let i in arr) {
    // Assumes the first element is the lowest one
    let indexOfMin = i;

    // Assure that the indexOfMin correspond to the index of the lowest element
    for (let j = i; j < arr.length; j++) {
      if (arr[j] < arr[indexOfMin]) indexOfMin = j;
    }

    // Atribute the lowest element to the first position only if the first element is not already the indexofMIn
    if (indexOfMin !== i) {
      const aux = arr[i];
      arr[i] = arr[indexOfMin];
      arr[indexOfMin] = aux;
    }
  }
  return arr;
}

function selectionSortSimple(arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = i; j < arr.length; j++) {
      if (arr[j] < arr[i]) {
        [arr[i], arr[j]] = [arr[j], arr[i]]; // swap
      }
    }
  }
  return arr;
}

module.exports = selectionSort;

console.log(selectionSort([10, 3, 2, -1, 0]));
console.log(selectionSortSimple([10, 3, 2, -1, 0]));
