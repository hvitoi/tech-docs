function reverseInteger(n) {
  const rev = n.toString().split("").reverse().join("");
  return parseInt(rev) * Math.sign(n);
}

// Testing
const test = require('node:test');
const assert = require('node:assert');

test('reversing an integer', () => {
  assert.strictEqual(reverseInteger(0), 0);
  assert.strictEqual(reverseInteger(5), 5);
  assert.strictEqual(reverseInteger(15), 51);
  assert.strictEqual(reverseInteger(90), 9);
  assert.strictEqual(reverseInteger(2359), 9532);

  assert.strictEqual(reverseInteger(-5), -5);
  assert.strictEqual(reverseInteger(-15), -51);
  assert.strictEqual(reverseInteger(-90), -9);
  assert.strictEqual(reverseInteger(-2359), -9532);
});
