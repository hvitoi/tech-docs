const exactMatch = new RegExp(/bob/);
const oneOrOtherPlusSomething = new RegExp(/(bob|alice)smith/);

const colorColour = new RegExp(/colou?r/); // "u" can occur 0 or 1 time
const colorrrrr = new RegExp(/color*/); // "r" can occur 0 or multiple times
const colorrrr = new RegExp(/color+/); // "r" can occur 1 or multiple times
const colorr = new RegExp(/color{2,6}/); // "r" can occur 2 to 6 times

const howAreYou = new RegExp(/How Are You\?/); // scape special caracters
const anyDigit = new RegExp(/\d/); // "\d" any digit (number)
const notDigit = new RegExp(/\D/);
const anyWord = new RegExp(/\w/); // "\w" any word (alphabetic)
const notWord = new RegExp(/\W/);

const negation = new RegExp(/[^abc]/); // everything that is not a + b or c

const vowels = new RegExp(/[aeiou]/gi); // matches every item inside of the square braces
const alphabetLetters = new RegExp(/[a-z]/gi); // character range
const nonLetterChars = new RegExp(/[^\w]/);
const filePath = new RegExp(/(\/.+)+$/);

// Option g: global (find all matches in the text)
// Option i: case insensitive
// Option m:
// Option s:
// Option y:
