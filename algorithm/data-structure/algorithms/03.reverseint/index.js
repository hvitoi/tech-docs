// --- Directions
//   Given an integer, return an integer that is the reverse
//   ordering of numbers.
// --- Examples
//   reverseInt(15) === 51
//   reverseInt(981) === 189
//   reverseInt(500) === 5
//   reverseInt(-15) === -51
//   reverseInt(-90) === -9
module.exports = reverseInt;

function reverseInt(n) {
  const rev = n.toString().split("").reverse().join("");
  return parseInt(rev) * Math.sign(n);
}

console.log(reverseInt(-590));
