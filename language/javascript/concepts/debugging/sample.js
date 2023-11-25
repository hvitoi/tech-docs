// Add letters to array (From first to last)
function reverseAddToArray(str) {
  const rev = [];
  for (let i = str.length - 1; i >= 0; i--) {
    debugger; // Pause the execution at that point'
    rev.push(str[i]);
  }
  return rev.join('');
}

console.log(reverseAddToArray('Henrique'));
