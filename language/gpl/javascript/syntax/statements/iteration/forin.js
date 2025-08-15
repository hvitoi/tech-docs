const arr = ["a", "b", "c"];
const obj = { a: 1, b: 2, c: 3 };

// Iterates by the index
for (let index in arr) {
  console.log(index, arr[index]);
}

// Iterates by the key in an object
for (let key in obj) {
  console.log(key, obj[key]);
}
