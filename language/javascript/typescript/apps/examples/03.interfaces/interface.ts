// The objects
const car = {
  name: 'civic',
  year: 2000,
  broken: true,
  summary(): string {
    return `My car is a ${this.name}.`;
  }
};

const drink = {
  color: 'brown',
  carbonated: true,
  sugar: 40,
  summary(): string {
    return `My drink has ${this.sugar} grams of sugar.`;
  }
};

// ---

// A interface defines a new type (template) for a object
interface Vehicle {
  name: string;
  year: number;
  broken: boolean;
  summary(): string; // A function that returns a string
}

const printVehicle = (vehicle: Vehicle): void => {
  console.log(`Name: ${vehicle.name}`);
  console.log(`Year: ${vehicle.year}`);
  console.log(`Broken: ${vehicle.broken}`);
};
printVehicle(car);

// --

interface Reportable {
  summary(): string;
}

const printSummary = (item: Reportable): void => {
  console.log(item.summary());
};
printSummary(car);
printSummary(drink);
