class Plane {
  color = "red";

  fly() {
    console.log("vrrr");
  }
}
// Instantiate
const plane = new Plane();

// Plane is actually a reference to a constructor!
console.log(plane);

// Methods are stored in the Plane prototype!
console.log(plane.prototype); // not good practice!
console.log(plane.__proto__); // not good practice!
console.log(Object.getPrototypeOf(plane));
