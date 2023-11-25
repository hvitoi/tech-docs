const res = "Hello there!".match(/[aeiou]/gi); // returns array of matched letters
const res2 = "!&654., ".match(/[a-z]/gi); // returns null (no match)
const res3 = "Hello there!".match(/[^\w]/gi); // non-letters chars (" ", "!")
const res4 = "/var/lib/".match(/(\/.+)+$/); // file path

console.log(res);
console.log(res2);
console.log(res3);
console.log(res4);

// Statement /[]/ matches every item inside of the square braces
// Option g: don't stop at first match
// Option i: case insensitive

const a = "aeiouhyhyhy".match(new RegExp(/[aeiou]/gi));
console.log(a);
