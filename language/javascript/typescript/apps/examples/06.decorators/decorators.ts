// testDecorator(Boat.prototype, 'pilot'); // Same effect as @testDecorator !
// target: { pilot: [Function (anonymous)] }
// key: pilot

@classDecorator
class Boat {
  @propertyDecorator
  color: string = 'red';

  @accessorDecorator
  get formattedColor(): string {
    return `This boats color is ${this.color}`;
  }

  // Apply decorator
  @logError // It is executed only ONE time when class is created and not when it is instantiated
  @logError2('Ops! The boat sunk in the ocean!')
  pilot(): never {
    throw new Error();
  }

  // Apply decorator for (multiple) arguments
  fly(
    @parameterDecorator speed: string,
    @parameterDecorator otherParam: boolean
  ): void {
    if (speed === 'fast') console.log('Flew!');
    else console.log('Too slow.');
  }
}

// DECORATOR FOR METHODS
function logError(target: any, key: string, desc: PropertyDescriptor): void {
  // desc is the configuration object (Object.getOwnPropertyDescriptor)
  const method = desc.value; // method receives the function itself!

  // Change the method value!
  desc.value = function () {
    try {
      method();
    } catch (e) {
      console.log('Ops, boat was sunk!'); // Boat will always sink because the method always throw error
    }
  };
}

// Wrapped decorators! The decorator is wrapping another function. Now argument can be passed in
function logError2(errorMessage: string) {
  return function (target: any, key: string, desc: PropertyDescriptor): void {
    const method = desc.value;
    desc.value = function () {
      try {
        method();
      } catch (e) {
        console.log(errorMessage);
      }
    };
  };
}

// DECORATOR FOR PROPERTIES
function propertyDecorator(target: any, key: string) {
  console.log(target); // the property cannot be accessible in the target because it is not defined in the constructor
  console.log(key);
}

// DECORATOR FOR ACCESSOR
function accessorDecorator(target: any, key: string) {
  console.log(key); // formattedColor (the key of the accessor)
}

// DECORATOR FOR FUNCTION ARGUMENTS
function parameterDecorator(target: any, key: string, index: number) {
  // index is the index of the argument
  console.log(key, index); // 'fly' and '0'
}

// DECORATOR FOR THE CLASS
function classDecorator(constructor: typeof Boat) {
  console.log('Constructor: ', constructor);
}

// Create an instance of boat
const boat = new Boat();
boat.pilot();
