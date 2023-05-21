// --- Directions
//   Write a function that returns the number of vowels
//   used in a string.  Vowels are the characters 'a', 'e'
//   'i', 'o', and 'u'.
// --- Examples
//   vowels('Hi There!') --> 3
//   vowels('Why do you ask?') --> 4
//   vowels('Why?') --> 0
module.exports = vowels1;

// Basic solution
function vowels1(str) {
  let count = 0;
  for (let char of str.toLowerCase()) {
    if (
      char === "a" ||
      char === "e" ||
      char === "i" ||
      char === "o" ||
      char === "u"
    )
      count++;
  }
  return count;
}

// With includes
function vowels2(str) {
  let count = 0;
  for (let char of str.toLowerCase()) {
    if ("aeiou".includes(char)) count++;
  }
  return count;
}

// With regex
function vowels3(str) {
  const volwelsArray = str.match(/[aeiou]/gi); // if matches are found, an array of matches is returned. If no match is found, return null
  const n = volwelsArray ? volwelsArray.length : 0;
  return n;
}

console.log(vowels1("Ola!"));
console.log(vowels2("Ola!"));
console.log(vowels3("Ola!"));
