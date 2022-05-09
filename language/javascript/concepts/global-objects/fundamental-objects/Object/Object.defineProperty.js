// Get the configuration object about a object key
// value: 'honda'
// writable: true // can update?
// enumerable: true // if it can be loop in a forin
// configurable: true

const car = { make: "honda", year: 2000 };
const info = Object.getOwnPropertyDescriptor(car, "make");
console.log(info);

// Change the configuration object
Object.defineProperty(car, "make", { writable: false });
car.make = "chevy"; // Doesn't update anymore!
console.log(car);

// Rename a field
if (old_key !== new_key) {
  Object.defineProperty(
    o,
    new_key,
    Object.getOwnPropertyDescriptor(o, old_key)
  );
  delete o[old_key];
}
