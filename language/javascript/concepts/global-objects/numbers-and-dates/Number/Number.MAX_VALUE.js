console.log(Number.MAX_VALUE);
// 2^53 - 1

const intNumber = 9007199254740990;
const bigIntNumber = 9007199254740990n;
console.log(intNumber + 3); // stuck at the MAX_SAFE_INTEGER
console.log(bigIntNumber + 3n); // go beyond MAX_SAFE_INTEGER
