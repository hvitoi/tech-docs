function isPalindromeByReverseAndCompare(str) {
  const rev = str.split("").reverse().join("");
  return str === rev;
}

function isPalindromeByComparingEachLetter(str) {
  return str.split("").every((char, i) => {
    return char === str[str.length - i - 1]; // Not ideal because it could stop in the middle (but it goes until the very last character)
  });
}

function isPalindromeByComparingEachLetterOptimized(str) {
  const len = str.length;
  for (let i = 0; i < len / 2; i++) {
    if (str[i] !== str[len - 1 - i]) return false; // Ideal, because it goes until the middle only
  }
  return true;
}

// Testing
const test = require('node:test');
const assert = require('node:assert');

test('a palindrome', () => {
  assert.strictEqual(isPalindromeByReverseAndCompare('abba'), true);
  assert.strictEqual(isPalindromeByComparingEachLetter('abba'), true);
  assert.strictEqual(isPalindromeByComparingEachLetterOptimized('abba'), true);
});


test('a non-palindrome', () => {
  assert.strictEqual(isPalindromeByReverseAndCompare(' abba'), false);
  assert.strictEqual(isPalindromeByComparingEachLetter(' abba'), false);
  assert.strictEqual(isPalindromeByComparingEachLetterOptimized(' abba'), false);
});
