// --- QUICK SORT - O(n*log(n)).
// we divide the list into halves every time, but we repeat the iteration N times(where N is the size of list).
// The running time consists of N loops (iterative or recursive) that are logarithmic, thus the algorithm is a combination of linear and logarithmic.

function swap(items, leftIndex, rightIndex) {
  const aux = items[leftIndex];
  items[leftIndex] = items[rightIndex];
  items[rightIndex] = aux;
}
function partition(items, left, right) {
  var pivot = items[Math.floor((right + left) / 2)], //middle element
    i = left, //left pointer
    j = right; //right pointer
  while (i <= j) {
    while (items[i] < pivot) {
      i++;
    }
    while (items[j] > pivot) {
      j--;
    }
    if (i <= j) {
      swap(items, i, j); //swapping two elements
      i++;
      j--;
    }
  }
  return i;
}
function quickSort(items, left, right) {
  var index;
  if (items.length > 1) {
    index = partition(items, left, right); //index returned from partition
    if (left < index - 1) {
      //more elements on the left side of the pivot
      quickSort(items, left, index - 1);
    }
    if (index < right) {
      //more elements on the right side of the pivot
      quickSort(items, index, right);
    }
  }
  return items;
}

// ---

module.exports = quickSort;

console.log(quickSort(items, 0, items.length - 1));
