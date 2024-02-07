// Check if it's the last element
function lastSubchunk(array, size) {
  const chunkedArray = [];

  for (let element of array) {
    const lastChunk = chunkedArray[chunkedArray.length - 1]; // get the last subchunk

    // if the last subchunk element is not yet full...
    if (lastChunk && lastChunk.length !== size) {
      lastChunk.push(element);
    }

    // if the subChunk is full (or lastChunk is undefined - in the first loop), push a new element to the array chunk
    else {
      chunkedArray.push([element]);
    }
  }

  return chunkedArray;
}

// Slice function
function chunkSlice(array, size) {
  const chunkedArray = [];

  // let index = 0;
  // while (index < array.length) {
  //   chunkedArray.push(array.slice(index, index + size));
  //   index += size;
  // }

  for (let i = 0; i < array.length; i = i + size) {
    chunkedArray.push(array.slice(i, i + size));
  }

  return chunkedArray;
}

// Subchunk feeding the chunk
function subChunk(array, size) {
  const chunkedArray = [];
  let i = 0;

  while (i < array.length) {
    const chunk = [];
    for (let j = 0; j < size; j++, i++) {
      if (!array[i]) break; // case the array ends
      chunk.push(array[i]);
    }
    chunkedArray.push(chunk);
  }

  return chunkedArray;
}

// chunk
function subChunk2(arr, size) {
  const chunked = [];
  let chunk = [];
  for (let item of arr) {
    if (chunk.length < size) chunk.push(item);
    else {
      chunked.push(chunk);
      chunk = [item];
    }
  }
  return chunked;
}

// chunk
function subChunk3(arr, chunkSize) {
  const chunkedArray = [];
  for (let i = 0; i < arr.length; i++) {
    const chunk = [];
    for (let j = i; j < i + chunkSize; j++) {
      if (!arr[j]) break;
      chunk.push(arr[j]);
    }
    chunkedArray.push(chunk);
    i = i + chunkSize - 1;
  }
  return chunkedArray;
}

// Testing

const test = require('node:test');
const assert = require('node:assert');

test('chunk divides an array of 10 elements with chunk size 2', () => {
  const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  const chunkSize = 2;
  const expected = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10]
  ];
  assert.deepEqual(subChunk3(arr, chunkSize), expected);
});

test('chunk divides an array of 3 elements with chunk size 1', () => {
  const arr = [1, 2, 3];
  const chunkSize = 1;
  const expected = [
    [1],
    [2],
    [3]
  ];
  assert.deepEqual(subChunk3(arr, chunkSize), expected);
});

test('chunk divides an array of 5 elements with chunk size 3', () => {
  const arr = [1, 2, 3, 4, 5];
  const chunkSize = 3;
  const expected = [
    [1, 2, 3],
    [4, 5]
  ];
  assert.deepEqual(subChunk3(arr, chunkSize), expected);
});

test('chunk divides an array of 13 elements with chunk size 5', () => {
  const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13];
  const chunkSize = 5;
  const expected = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13]
  ];
  assert.deepEqual(subChunk3(arr, chunkSize), expected);
});
