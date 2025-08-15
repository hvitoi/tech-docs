const test = require('node:test');
const assert = require('node:assert');

const sum = (num1, num2) => num1 + num2;

test('adding numbers', () => {
  const actual = sum(1, 2);
  const expected = 3;
  assert.strictEqual(actual, expected);
})

// You can run this test directly with `node file.test.js`
// Or you can run from the root of the project to automatically find all test files `node --test`
