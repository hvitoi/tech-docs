// GENERICS WITH CLASSES

class ArrayOfAnything<T> {
  constructor(public collection: T[]) {}
  get(index: number): T {
    return this.collection[index];
  }
  getAll() {
    return this.collection;
  }
}
const arrayOfNumber = new ArrayOfAnything<number>([1, 2, 3]);
const arrayOfNumber2 = new ArrayOfAnything([1, 2, 3]); // the type can be omitted! (inference)
arrayOfNumber.get(0);
arrayOfNumber2.get(0);

const arrayOfString = new ArrayOfAnything<string>(['a', 'b', 'c']);
arrayOfString.get(0);

// GENERICS WITH FUNCTIONS
function printAnything<T>(arr: T[]): void {
  for (let item of arr) console.log(item);
}
printAnything<string>(arrayOfString.getAll());
printAnything<number>(arrayOfNumber.getAll());
printAnything(arrayOfNumber.getAll()); // type identified by inference

// Generic Constraints
class Car {
  print() {
    console.log('I am a car');
  }
}
class House {
  print() {
    console.log('I am a house');
  }
}

interface Printable {
  print(): void;
}

// Type T promises to have the methods defined in Printable
function printHousesOrCars<T extends Printable>(arr: T[]): void {
  for (let item of arr) item.print();
}
printHousesOrCars<Printable>([new House(), new Car()]);

// GENERICS WITH METHODS
class Attributes<T> {
  constructor(private data: T) {}

  // K can be any of the 'keys' in T!
  // The function returns a value of type Object['key']
  get<K extends keyof T>(key: K): T[K] {
    return this.data[key];
  }
}

// GENERICS WITH INTERFACES
interface Attributes<T> {
  set(value: T): void;
  getAll(): T;
  get<K extends keyof T>(key: K): T[K];
}
