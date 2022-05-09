// --- Directions
//   Given a string, return a new string with
//   the reversed order of characters
// --- Examples
//   reverse('apple') === 'leppa'
//   reverse('hello') === 'olleh'
//   reverse('Greetings!') === '!sgniteerG'
module.exports = reverseMethod;

// Split, reverse and join
function reverseMethod(str) {
  return str.split("").reverse().join("");
}

// Add letters to array (from last to first)
function addToArray(str) {
  const rev = [];
  for (let i in str) {
    rev[str.length - i - 1] = str[i];
  }
  return rev.join("");
}

// Add letters to array (From first to last)
function addToArray2(str) {
  const rev = [];
  for (let i = str.length - 1; i >= 0; i--) {
    rev.push(str[i]);
  }
  return rev.join("");
}

// Add letters to string
function addToString(str) {
  let rev = "";
  for (let char of str) {
    rev = char + rev;
  }
  return rev;
}

// Reduce
function reduceString(str) {
  return str.split("").reduce((rev, char) => char + rev, ""); // '' is the inital 'rev' value
}

console.log(reverseReverseMethod("Henrique"));
console.log(addToArray("Henrique"));
console.log(addToArray2("Henrique"));
console.log(addToString("Henrique"));
console.log(reduceString("Henrique"));
