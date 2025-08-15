/**
 * MATH
 */

const calculateTip = (total, tipPercent = 0.25) => total + total * tipPercent;

const fahrenheitToCelsius = (temp) => {
  return (temp - 32) / 1.8;
};

const celsiusToFahrenheit = (temp) => {
  return temp * 1.8 + 32;
};

const add = (a, b) => {
  // add with timeout simulates a db query
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (a < 0 || b < 0) {
        reject("Numbers must be non-negative");
      }
      resolve(a + b);
    }, 1000);
  });
};

module.exports = {
  calculateTip,
  fahrenheitToCelsius,
  celsiusToFahrenheit,
  add,
};
const {
  calculateTip,
  fahrenheitToCelsius,
  celsiusToFahrenheit,
  add,
} = require("../src/math");

test("30% tip", () => {
  const total = calculateTip(10, 0.3);
  expect(total).toBe(13);
});

test("Default 25% tip", () => {
  const total = calculateTip(10);
  expect(total).toBe(12.5);
});

test("Fahrenheit to Celsius", () => {
  const total = fahrenheitToCelsius(32);
  expect(total).toBe(0);
});

test("Celsius to Fahrenheit", () => {
  const total = celsiusToFahrenheit(0);
  expect(total).toBe(32);
});

test("Add 2 numbers - Promise", (done) => {
  add(2, 3).then((sum) => {
    expect(sum).toBe(5);
    done();
  });
});

test("Add 2 numbers - async-await", async (done) => {
  const sum = await add(10, 22);
  expect(sum).toBe(32);
});
