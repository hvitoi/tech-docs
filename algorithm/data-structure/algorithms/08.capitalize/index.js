// --- Directions
//   Write a function that accepts a string.  The function should
//   capitalize the first letter of each word in the string then
//   return the capitalized string.
// --- Examples
//   capitalize('a short sentence') --> 'A Short Sentence'
//   capitalize('a lazy fox') --> 'A Lazy Fox'
//   capitalize('look, it is working!') --> 'Look, It Is Working!'
module.exports = splitWordsAndCapitalizeFirst;

// Split the string and capitalize each first letter
function splitWordsAndCapitalizeFirst(str) {
  // Split the string into an array
  let words = str.split(" ");

  // Map the words array to upper case the first letters
  const capitalized = words.map(
    (word) => word[0].toUpperCase() + word.slice(1)
  );

  // Return the joined array
  return capitalized.join(" ");
}

// Checking if the left letter is a blank space or undefined
function checkIfEmptySpace(str) {
  let capitalized = "";
  for (let i in str) {
    if (!str[i - 1] || str[i - 1] == " ") {
      capitalized = capitalized + str[i].toUpperCase();
    } else {
      capitalized = capitalized + str[i];
    }
  }
  return capitalized;
}

// Checking if the left letter is a blank space or undefined
function matchNonLetters(str) {
  let cap = "";
  for (let i in str) {
    if (!str[i - 1] || !str[i - 1].match(/[a-z]/gi)) {
      cap = cap + str[i].toUpperCase();
    } else {
      cap = cap + str[i];
    }
  }
  return cap;
}

console.log(splitWordsAndCapitalizeFirst("my name is henrique"));
console.log(checkIfEmptySpace("my name is henrique"));
console.log(matchNonLetters("my name is henrique, nice to meet you! ok?"));
