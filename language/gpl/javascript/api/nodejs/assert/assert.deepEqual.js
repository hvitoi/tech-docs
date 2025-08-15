const test = require('node:test');
const assert = require('node:assert');

const sum = (num1, num2) => num1 + num2;


// "equal" ensures only that values have same structure but are not reference-equal
test('adding numbers', () => {
  const actual = [1, 2, 3];
  const expected = [1, 2, 3];
  assert.deepEqual(actual, expected);
})
