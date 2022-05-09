// Array-like structure to represent an object. Information is lost

const drink = {
  color: 'brown',
  carbonated: true,
  sugar: 40
};

// The annotation turns the array into a tuple!
const pepsi: [string, boolean, number] = ['brown', true, 40];

// Type alias creation
type Drink = [string, boolean, number];
const fanta: Drink = ['orange', true, 50];
