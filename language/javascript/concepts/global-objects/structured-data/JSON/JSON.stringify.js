const obj = { a: 1, b: 2 };

console.log(JSON.stringify(obj));
console.log(JSON.parse(JSON.stringify(obj)));

// Change the behavior of the stringify function
const person = {
  name: "alex",
  toJSON() {
    return 1;
  },
};
const stringifiedPerson = JSON.stringify(person); //Returns 1
console.log(stringifiedPerson);
