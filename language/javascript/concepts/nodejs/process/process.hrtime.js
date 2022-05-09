// The process.hrtime() method to measure code execution time which
// returns array which include current high-resolution real time in
// a [seconds, nanoseconds]

let obj = { a: 1 };
for (let i = 0; i < 20; i++) {
  obj = { obj1: obj, obj2: obj }; // Doubles in size each iter
}

// ---
var before = process.hrtime();
const str = JSON.stringify(obj);
var took = process.hrtime(before);
console.log("JSON.stringify: " + took);

// ---

var before = process.hrtime();
const pos = str.indexOf("nomatch");
var took = process.hrtime(before);
console.log("String.prototype.indexOf: " + took);

// ---

var before = process.hrtime();
const parse = JSON.parse(str);
var took = process.hrtime(before);
console.log("JSON.parse: " + took);
