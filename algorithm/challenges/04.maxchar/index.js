// --- Directions
//   Given a string, return the character that is most
//   commonly used in the string.
// --- Examples
//   maxChar("abcccccccd") === "c"
//   maxChar("apple 1231111") === "1"
module.exports = maxChar;

function maxChar(str) {
  const charMap = {};
  let maxChar = "";
  let maxOcc = 0;

  // Create the characters map
  for (let char of str) {
    if (charMap[char]) charMap[char]++;
    else charMap[char] = 1;
    //charMap[char] ? charMap[char]++ : (charMap[char] = 1);
    //charMap[char] = charMap[char] + 1 || 1;
  }

  // Check the most frequent char
  for (let key in charMap) {
    if (charMap[key] > maxOcc) {
      maxChar = key;
      maxOcc = charMap[key];
    }
  }

  return maxChar;
}

console.log(maxChar("Henrique"));
