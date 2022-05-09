// npm i reflect-metadata

// - `"experimentalDecorators": true` and `"emitDecoratorMetadata": true` must be enabled in tsconfig.json
// npm i reflect-metadata

import "reflect-metadata"; // a single variable to global scope (Reflect)

const plane = {
  color: "red",
};

// The metadata is secret and it can only be accessible through the reflect-metadata package

// Create metadata. // key - value - object
Reflect.defineMetadata("note", "Hi there!", plane);
Reflect.defineMetadata("height", 10, plane);
console.log(plane); // the 'note' and 'height' props will not appear

// Retrieve metadata
const note = Reflect.getMetadata("note", plane); // Get the 'note' from the object
console.log(note);

// ---

// Associate metadata with a property
Reflect.defineMetadata("specificNote", "Hey again!", plane, "color");
Reflect.getMetadata("specificNote", plane, "color");
