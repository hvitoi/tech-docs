function reverse(str) {
  let rev = "";
  for (let char of str) {
    debugger; // Freezes the code whenever 'debugger;' is found
    rev = char + rev;
  }
  return rev;
}

reverse("Henrique");

// Start debugging
// node inspect debugger.js

// Go to next moment
// debug> continue          debug> c

// repl: read/eval/print loop
// debug> repl
// Opens a JS console to inspect variables!
// Ctrl+C to exit the repl mode
