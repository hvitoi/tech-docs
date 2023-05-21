const foo = ["a", "b", "c"];

// returns an Iterator with the keys of the array
const bar = foo.keys();

// logging
console.log(bar);
for (const el of bar) {
  console.log(el); // 0 .. 1 ..
}
