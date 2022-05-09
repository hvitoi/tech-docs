// immutable object

const obj = Object.freeze({ foo: "Can't mutate me" });
const arr = Object.freeze([1, 2, 3]);

obj.foo = "a";
arr.push[4];

console.log(obj); // unchanged
console.log(arr); // unchanged
