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


console.log(bubbleSort([10, 3, 2, -1, 0]));
