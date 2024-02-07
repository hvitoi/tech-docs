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

// Testing
const test = require('node:test');
const assert = require('node:assert');

test('capitalizes the first letter of every word in a sentence', () => {
  assert.strictEqual(
    splitWordsAndCapitalizeFirst("my name is henrique, nice to meet you! ok?"),
    "My Name Is Henrique, Nice To Meet You! Ok?");

  assert.strictEqual(
    checkIfEmptySpace("my name is henrique, nice to meet you! ok?"),
    "My Name Is Henrique, Nice To Meet You! Ok?");

  assert.strictEqual(
    matchNonLetters("my name is henrique, nice to meet you! ok?"),
    "My Name Is Henrique, Nice To Meet You! Ok?");

});
