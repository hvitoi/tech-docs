// Basic solution
function vowels1(str) {
  let count = 0;
  for (let char of str.toLowerCase()) {
    if (
      char === "a" ||
      char === "e" ||
      char === "i" ||
      char === "o" ||
      char === "u"
    )
      count++;
  }
  return count;
}

// With includes
function vowels2(str) {
  let count = 0;
  for (let char of str.toLowerCase()) {
    if ("aeiou".includes(char)) count++;
  }
  return count;
}

// With regex
function vowels3(str) {
  const volwelsArray = str.match(/[aeiou]/gi); // if matches are found, an array of matches is returned. If no match is found, return null
  const n = volwelsArray ? volwelsArray.length : 0;
  return n;
}

// Testing
const test = require('node:test');
const assert = require('node:assert');

test('returns the number of vowels used', () => {
  assert.strictEqual(vowels1('aeiou'), 5);
  assert.strictEqual(vowels1('AEIOU'), 5);
  assert.strictEqual(vowels1('abcdefghijklmnopqrstuvwxyz'), 5);
  assert.strictEqual(vowels1('bcdfghjkl'), 0);
});
