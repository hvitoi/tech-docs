// Every Symbol() call is guaranteed to return a unique Symbol

let sym1 = Symbol();
let sym2 = Symbol("foo");
let sym3 = Symbol("foo");

Symbol("foo") === Symbol("foo"); // false
