const foo = require("./index");

test("Test 1", () => {
  const codeList = [
    ["apple", "apple"],
    ["banana", "anything", "banana"],
  ];
  const shoppingCart = [
    "orange",
    "apple",
    "apple",
    "banana",
    "orange",
    "banana",
  ];
  const res = foo(codeList, shoppingCart);
  expect(res).toEqual(1);
});

test("Test 2", () => {
  const codeList = [
    ["apple", "apple"],
    ["banana", "anything", "banana"],
  ];
  const shoppingCart = ["banana", "orange", "banana", "apple", "apple"];
  const res = foo(codeList, shoppingCart);
  expect(res).toEqual(0);
});

test("Test 3", () => {
  const codeList = [
    ["apple", "apple"],
    ["banana", "anything", "banana"],
  ];
  const shoppingCart = ["apple", "banana", "apple", "orange", "banana"];
  const res = foo(codeList, shoppingCart);
  expect(res).toEqual(0);
});

test("Test 4", () => {
  const codeList = [
    ["apple", "apple"],
    ["apple", "apple", "banana"],
  ];
  const shoppingCart = ["apple", "apple", "apple", "banana"];
  const res = foo(codeList, shoppingCart);
  expect(res).toEqual(0);
});
