const family = [
  {
    name: 'Henrique',
    age: 19
  },
  {
    name: 'Laís',
    age: 28
  },
  {
    name: 'Luiz',
    age: 30
  },
  {
    name: 'Simone',
    age: 17
  }
];
const isAdult = (person) => person.age >= 18;

// Return true if at least a person is adult
const hasAdult = family.some(isAdult);
console.log(hasAdult);
