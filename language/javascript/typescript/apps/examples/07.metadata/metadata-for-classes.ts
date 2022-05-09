import 'reflect-metadata';

@printMetadata
class Plane {
  color: string = 'red';

  @markFunction('My little secret!')
  fly(): void {
    console.log('vrrr');
  }
}

// A decorator to the method (it adds a metadata to the method)
function markFunction(secretInfo: string) {
  return function (target: Plane, key: string) {
    // target is the Plane prototype (Plane class)!! Which is an object
    Reflect.defineMetadata('secret', secretInfo, target, key); // add a metadata for the fly method
  };
}

// Retrieve the metadata
const secret = Reflect.getMetadata('secret', Plane.prototype, 'fly');
console.log(secret);

// ---
// A decorator to the class itself!! It prints all the metadata of this class
function printMetadata(target: typeof Plane) {
  // typeof Plane is a reference to the constructor of PLane!!
  // Loop through all the methods in the class!
  for (let key in target.prototype) {
    const secret = Reflect.getMetadata('secret', target.prototype, key); // key: fly
    console.log(secret);
  }
}
