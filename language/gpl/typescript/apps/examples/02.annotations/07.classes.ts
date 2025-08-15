class Vehicle {
  // A property!
  color: string;

  // A method!
  protected honk(): void {
    console.log('Beep!');
  }

  // A constructor is run when an instance is created
  constructor(color: string) {
    this.color = color;
  }
  // Equivalent constructor
  // constructor(public color: string) {}
}
const vehicle = new Vehicle('orange'); // Pass the parameters to the constructor function
console.log(vehicle.color);

// Inheritance
class Car extends Vehicle {
  constructor(public wheels: number, color: string) {
    super(color); // Calls the constructor from the parent!
  }

  private drive(): void {
    console.log('Vrum Vrum!'); // Replaces the original drive method
  }

  startDrivingProcess(): void {
    this.drive(); // Calling a private method (this class)
    this.honk(); // Calling a protected method (parent class)
  }
}
const car = new Car(4, 'green');
car.startDrivingProcess();

// Modifiers: public by default
// Public: Methods can be called anywhere, anytime
// Private: Method can only be called by other methods in THIS class
// Protected: Method can be called by other methods in THIS class or methods in the CHILD class
