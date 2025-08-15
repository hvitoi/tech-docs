const text = "-0590asd"; // non-numbers characters will be removed

// Transform a string into a number
number = parseInt(text); // base 10 by default
numberBase10 = parseInt(text, 10); // specify the input base (10 for decimal)
numberBase2 = parseInt("00101", 2); // specify the input base (2 for binary)

console.log(number);
console.log(numberBase10);
console.log(numberBase2);
