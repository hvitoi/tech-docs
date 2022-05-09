// Check if element is an Object
let obj = { author: "KDL" };
let list = [obj, obj];

let op = list.filter((data) => data instanceof Object); // filter only Objects
console.log(op);

// Check if element is an String

let strA = new String("Krunal");
let strB = new String("Ankit");
let strC = new String("Rushabh");

let arr = [strA, strB, strC];

let arrContainString = arr.filter((element) => element instanceof String); // filter only Strings
console.log(arrContainString);
