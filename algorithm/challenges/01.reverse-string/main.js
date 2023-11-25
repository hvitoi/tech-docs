// Split, reverse and join
function reverseStringSimple(str) {
  return str.split("").reverse().join("");
}

// Add letters to array (from last to first)
function reverseStringWithArray(str) {
  const rev = [];
  for (let i in str) {
    rev[str.length - i - 1] = str[i];
  }
  return rev.join("");
}

// Add letters to array (From first to last)
function reverseStringWithArrayInverse(str) {
  const rev = [];
  for (let i = str.length - 1; i >= 0; i--) {
    rev.push(str[i]);
  }
  return rev.join("");
}

// Add letters to string
function reverseStringWithString(str) {
  let rev = "";
  for (let char of str) {
    rev = char + rev;
  }
  return rev;
}

// Reduce
function reverseStringWithReduce(str) {
  return str.split("").reduce((rev, char) => char + rev, ""); // '' is the inital 'rev' value
}

// Testing
const test = require('node:test');
const assert = require('node:assert');

test('reversing a string', () => {
  assert.strictEqual(reverseStringSimple('Henrique Vitoi'), "iotiV euqirneH");
  assert.strictEqual(reverseStringWithArray('Henrique Vitoi'), "iotiV euqirneH");
  assert.strictEqual(reverseStringWithArrayInverse('Henrique Vitoi'), "iotiV euqirneH");
  assert.strictEqual(reverseStringWithString('Henrique Vitoi'), "iotiV euqirneH");
  assert.strictEqual(reverseStringWithReduce('Henrique Vitoi'), "iotiV euqirneH");
});
