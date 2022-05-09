// --- Directions
//   Given a string, return true if the string is a palindrome
//   or false if it is not.  Palindromes are strings that
//   form the same word if it is reversed. *Do* include spaces
//   and punctuation in determining if the string is a palindrome.
// --- Examples
//   palindrome("abba") === true
//   palindrome("abcdefg") === false
module.exports = compareEachLetterMiddle;

function reverseAndCompare(str) {
  const rev = str.split("").reverse().join("");
  return str === rev;
}

function compareEachLetterAll(str) {
  return str.split("").every((char, i) => {
    return char === str[str.length - i - 1]; // Not ideal because it could stop in the middle (but it goes until the very last character)
  });
}

function compareEachLetterMiddle(str) {
  const len = str.length;
  for (let i = 0; i < len / 2; i++) {
    if (str[i] !== str[len - 1 - i]) return false; // Ideal, because it goes until the middle only
  }
  return true;
}

function palindromeIndex(str) {
  if (str === str.split("").reverse().join("")) return -1;

  for (let i = 0; i < str.length; i++) {
    const chunk = str.split("");
    chunk.splice(i, 1);
    if (chunk.join("") === chunk.reverse().join("")) return i;
  }

  return -1;
}

console.log(reverseAndCompare("abba"));
console.log(compareEachLetterAll("abba"));
console.log(compareEachLetterMiddle("abba"));
console.log(palindromeIndex("abbak"));
