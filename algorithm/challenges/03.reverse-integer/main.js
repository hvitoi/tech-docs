function reverseInt(n) {
  const rev = n.toString().split("").reverse().join("");
  return parseInt(rev) * Math.sign(n);
}

// Testing
const test = require('node:test');
const assert = require('node:assert');

test('reversing an integer', () => {
  assert.strictEqual(reverseInt(0), 0);
  assert.strictEqual(reverseInt(5), 5);
  assert.strictEqual(reverseInt(15), 51);
  assert.strictEqual(reverseInt(90), 9);
  assert.strictEqual(reverseInt(2359), 9532);

  assert.strictEqual(reverseInt(-5), -5);
  assert.strictEqual(reverseInt(-15), -51);
  assert.strictEqual(reverseInt(-90), -9);
  assert.strictEqual(reverseInt(-2359), -9532);
});
