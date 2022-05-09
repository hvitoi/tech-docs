const { chooseFleets } = require("./app");

describe("chooseFleets() method", () => {
  test("function is defined", () => {
    expect(chooseFleets).toBeDefined();
  });

  test("correct output for array size 3", () => {
    expect(chooseFleets([4, 5, 6])).toEqual([2, 0, 2]);
  });

  test("correct output for array size 6", () => {
    expect(chooseFleets([4, 5, 6, 9, 10])).toEqual([2, 0, 2, 0, 3]);
  });

  test("correct output for array size 7", () => {
    expect(chooseFleets([4, 5, 6, 9, 10, 22])).toEqual([2, 0, 2, 0, 3, 6]);
  });
});
