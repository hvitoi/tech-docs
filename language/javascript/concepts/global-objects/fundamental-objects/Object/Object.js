// Object is a structure of key-value pairs
// The 'key' is always a string

/**
 * Object creation
 */
var obj = {}; // Empty object
var obj = new Object(); // Empty object
var obj = Object.create(null); // Empty object

var dog = {
  name: "Pingo", // name is a string "name"
  legs: 4,
  "number of tails": 1,
  friends: ["Everything"],
  16: "Qualquer coisa", // 16 is a string "16"
};

/**
 * Object access
 */
console.log(dog.name);
console.log(dog["number of tails"]);
console.log(dog[16]); // "16"
console.log(dog["16"]); // same output

/**
 * Create key
 */
dog.latir = "aw aw";
dog["miar"] = false;

/**
 * Delete key
 */
delete dog.miar;
console.log(dog.hasOwnProperty("miar")); // Check if the property exists

/**
 * Object destructuring
 */
var obj = {
  x: 3.6,
  y: 7.4,
  z: 6.5,
};

var { x: a, y: b, z: c, k: d = 9 } = obj;
console.log(a, b, c, d); // k doesn't exist so it receives the default value (9)
