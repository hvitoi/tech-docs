var map = new Map([
  ["a", 1],
  ["b", 2],
]);

map.forEach((value, key) => console.log(`key: ${key}, value: ${value}`));
for (const item of map) console.log(item);
for (const [key, value] of map) console.log(`key: ${key}, value: ${value}`);

//console.log(typeof obj[Symbol.iterator]); // undefined
console.log(typeof map[Symbol.iterator]); // function
