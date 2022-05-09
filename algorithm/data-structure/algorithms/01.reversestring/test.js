const reverse = require('./index');

test('Function exists', () => {
  expect(reverse).toBeDefined();
});

test('Function reverses a string', () => {
  expect(reverse('abcd')).toEqual('dcba');
});

test('Function reverses a string with spaces', () => {
  expect(reverse('  abcd')).toEqual('dcba  ');
});
