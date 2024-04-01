function famousChar(str) {
  const charMap = {};
  let famousChar = "";
  let famousCharOccurences = 0;

  // Create the characters map
  for (let char of str) {
    charMap[char] = charMap[char] + 1 || 1;
    //charMap[char] ? charMap[char]++ : (charMap[char] = 1);
    // if (charMap[char]) charMap[char]++;
    // else charMap[char] = 1;
  }

  // Check the most frequent char
  for (let char in charMap) {
    if (charMap[char] > famousCharOccurences) {
      famousChar = char;
      famousCharOccurences = charMap[char];
    }
  }

  return famousChar;
}

// Testing

const test = require('node:test');
const assert = require('node:assert');

test('the most common char in a word', () => {
  assert.strictEqual(famousChar("a"), "a");
  assert.strictEqual(famousChar("abcdefghijklmnaaaaa"), "a");
  assert.strictEqual(famousChar("ab1c1d1e1f1g1"), "1");
});
