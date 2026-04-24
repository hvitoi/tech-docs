function fizzBuzz(n) {
  return Array.from({ length: n }, (_, i) => i + 1)
    .map((i) => {
      if (i % 3 === 0 && i % 5 === 0) return "fizzbuzz";
      else if (i % 3 === 0) return "fizz";
      else if (i % 5 === 0) return "buzz";
      else return i;
    });
}

// Testing

const test = require('node:test');
const assert = require('node:assert');

test('FizzBuzz for 5', () => {
  assert.deepEqual(fizzBuzz(15),
    [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizzbuzz']);
});
