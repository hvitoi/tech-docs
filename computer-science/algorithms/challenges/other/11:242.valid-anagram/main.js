function anagramCharMap(strA, strB) {
  // Clean strings
  strA = strA.replace(/[^\w]/g, "").toLowerCase();
  strB = strB.replace(/[^\w]/g, "").toLowerCase();

  // charMaps
  const charMapA = {};
  const charMapB = {};

  // Populate charMaps
  for (let char of strA) {
    charMapA[char] = charMapA[char] + 1 || 1;
  }
  for (let char of strB) {
    charMapB[char] = charMapB[char] + 1 || 1;
  }

  // Comparison of number of keys
  if (Object.keys(charMapA).length !== Object.keys(charMapB).length) {
    return false;
  }

  // Comparison of items in charMaps
  for (let i in charMapA) {
    if (!charMapB[i]) return false; // This line is unnecessary
    if (charMapA[i] !== charMapB[i]) return false;
  }

  // Return true if all comparisons are passed
  return true;
}

// Sort Alphabetically
function anagramSorted(strA, strB) {
  // Cleanup strings and sort alphabetically
  strA = strA.replace(/[^\w]/g, "").toLowerCase().split("").sort().join("");
  strB = strB.replace(/[^\w]/g, "").toLowerCase().split("").sort().join("");

  // Check string length
  if (strA.length !== strB.length) return false; // Not necessary

  // Check each char of the string
  if (strA !== strB) return false;

  // Strings are anagrams if all comparisons are passed
  return true;
}

// Testing
const test = require("node:test");
const assert = require("node:assert");

test('anagrams', () => {
  assert.strictEqual(anagramCharMap('hello', 'llohe'), true);
  assert.strictEqual(anagramCharMap('Whoa! Hi!', 'Hi! Whoa!'), true);

  assert.strictEqual(anagramCharMap('One One', 'Two two two'), false);
  assert.strictEqual(anagramCharMap('One one', 'One one c'), false);
  assert.strictEqual(anagramCharMap('A tree, a life, a bench', 'A tree, a fence, a yard'), false);
});
