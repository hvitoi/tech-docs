class Food {
  // Property
  foodName = "No food yet!";

  // Static property
  static description = "This class represents foods!";

  // The constructor is run upon instantiating the class object
  constructor(name) {
    this.foodName = name; // create or assign value to a property
  }

  // Method: Methods in JS classes are stored in the prototype
  printName() {
    console.log(this.foodName);
  }

  // Static method
  static printDescription() {
    console.log(this.description);
  }
}

// Instantiation and call of methods
food = new Food("egg");
food.printName();

// Invoking static method
Food.printDescription(); // can be invoked without instantiating

// Create a new method by means of the prototype
Food.prototype.printHello = () => {
  console.log("Hello!!!");
};
food.printHello();
// Prototype of the class (properties won't appear because they are created in the constructor).
// Prototype only stores methods definitions

// ---
// 'THIS' statement

class Color {
  constructor(colorName) {
    this.name = colorName;
  }

  // Normal function
  normalPrint() {
    console.log(this.name);
  }

  // Arrow function
  arrowPrint = () => {
    console.log(this.name);
  };
}

const color = new Color("red"); // Instantiate
const normalPrint = color.normalPrint; // Destructure
const arrowPrint = color.arrowPrint; // Destructure

// Normal function print
color.normalPrint(); // return 'red' ... OK
//normalPrint(); // return 'undefined' ... ERROR

// Arrow function print
color.arrowPrint(); // return 'red' ... OK
arrowPrint(); // return 'red' ... POK

// THIS in arrow functions refers to the object instantiated
// THIS in normal function refers to what is written to the left

/**
 * Getter (accessor) & Setter
 */

class BankAccount {
  name;
  amount;

  constructor(name) {
    this.name = name;
  }

  get aamount() {
    return this.amount;
  }

  set aamount(value) {
    if (!value) {
      throw "Invalid data";
    }
    this.amount = value;
  }

  get lol() {
    return "lol";
  }
}

const account = new BankAccount("Henry");
console.log(account.name);
account.aamount = "1000";
console.log(account.aamount);

console.log(account.lol);
