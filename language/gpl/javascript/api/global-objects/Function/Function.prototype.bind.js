// Currying is the process of taking some function that accepts multiple arguments,
// and turning it into a sequence of functions, each accepting a single argument.
// Or put another way, to transform a function with multiple arguments into a chain
// of single-argument functions.

function giveMe3(item1, item2, item3) {
  return `
    1: ${item1}
    2: ${item2}
    3: ${item3}
  `;
}

// return a partial function, removing one argument at a time
const giveMe2 = giveMe3.bind(null, "rock");
const giveMe1 = giveMe2.bind(null, "paper");
const result = giveMe1("scissors");

console.log(result);
// 1: rock
// 2: paper
// 3: scissors

const giveMe2Arrow = (b, c) => giveMe3("rock", b, c);
const giveMe1Arrow = (c) => giveMe2Arrow("paper", c);
const resultArrow = giveMe1Arrow("scissors");

console.log(result);
// 1: rock
// 2: paper
// 3: scissors

// ---

function whodis() {
  console.log(this);
}

const jeff = {
  face: "🥰",
};

// explicitly set a "this" for a function. "this" is now the object "jeff"
const itsJeff = whodis.bind(jeff);
itsJeff();
