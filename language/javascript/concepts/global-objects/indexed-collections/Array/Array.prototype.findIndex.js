// O(N)

// Returns the index of the first element that matches the criteria
// Similar to find, but instead of returning the value, returns the index
function isPrime(element, index, array) {
  var start = 2;
  while (start <= Math.sqrt(element)) {
    if (element % start++ < 1) {
      return false;
    }
  }
  return element > 1;
}

console.log([4, 6, 8, 12].findIndex(isPrime)); // -1, não encontrado
console.log([4, 6, 7, 12].findIndex(isPrime)); // 2
