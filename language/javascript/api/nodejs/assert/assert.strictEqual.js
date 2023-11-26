const test = require('node:test');
const assert = require('node:assert');

const sum = (num1, num2) => num1 + num2;


// strictEqual ensures that the variable is equal and the same reference in memory (const)
test('adding numbers', () => {
  const actual = sum(1, 2);
  const expected = 3;
  assert.strictEqual(actual, expected);
})
