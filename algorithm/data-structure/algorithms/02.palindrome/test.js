const palindrome = require('./index');

test('Palindrome function is defined', () => {
  expect(typeof palindrome).toEqual('function');
});

test('"abba" is a palindrome', () => {
  expect(palindrome('abba')).toBeTruthy();
});

test('" abba" is not a palindrome', () => {
  expect(palindrome(' abba')).toBeFalsy();
});

test('"aba " is not a palindrome', () => {
  expect(palindrome('aba ')).toBeFalsy();
});

test('"greetings" is not a palindrome', () => {
  expect(palindrome('greetings')).toBeFalsy();
});

test('"1000000001" a palindrome', () => {
  expect(palindrome('1000000001')).toBeTruthy();
});

test('"Fish hsif" is not a palindrome', () => {
  expect(palindrome('Fish hsif')).toBeFalsy();
});

test('"pennep" a palindrome', () => {
  expect(palindrome('pennep')).toBeTruthy();
});
