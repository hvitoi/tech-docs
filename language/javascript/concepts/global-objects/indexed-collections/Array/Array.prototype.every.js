const family = [
  {
    name: "Henrique",
    age: 19,
  },
  {
    name: "Laís",
    age: 28,
  },
  {
    name: "Luiz",
    age: 30,
  },
  {
    name: "Simone",
    age: 17,
  },
];
const isAdult = (person) => person.age >= 18;

// Returns: true or false. 'true' only is every item in the loop is true
const isEveryoneAdult = family.every(isAdult);
console.log(isEveryoneAdult);

// Palindrome
function compareEachLetter(str) {
  return str.split("").every((char, i) => {
    return char === str[str.length - i - 1];
  });
}

// ---
let chunk = [19, 21, 29, 46];
let arr = [2, 6, 18, 19, 29, 46, 53, 21];

// check if every element in chunk in inside of arr
let op = chunk.every((element) => arr.indexOf(element) > -1);
console.log(op);

// ---

// compare arrays
array1.length === array2.length &&
  array1.every((value, index) => value === array2[index]);
