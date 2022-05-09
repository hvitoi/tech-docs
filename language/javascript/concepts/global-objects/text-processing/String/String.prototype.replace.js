const word = "Hi there!!!!";

// Replace special characters with nothing ''
const newword = word.replace(/[^\w]/g, "");
console.log(newword);

// Replace a to z characters with nothing ''
const newword2 = word.replace(/[a-z]/gi, ""); // g: don't stop after first match, i: case insensitive
console.log(newword2);

// Replace vowels characters with nothing ''
const newword3 = word.replace(/[aeiou]/gi, "");
console.log(newword3);
