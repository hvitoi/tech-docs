const person = {
  name: "Henrique",
  age: 26,
  height: 181,
};

const update = {
  age: 27, // Will be updated
  weight: 75, // Will be created
};

// Copy all the props from the 2nd object into the first object
Object.assign(person, update);
console.log(person);

// console.log({ ...person, ...update }); // Same effect with ES6
