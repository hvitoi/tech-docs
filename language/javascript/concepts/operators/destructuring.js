/**
 * Arrays
 */

var [one, two] = [1, 2, 3, 4];
var [, , three, four] = [1, 2, 3, 4];
var [one, ...rest] = [1, 2, 3, 4];
var [one, two, three, four, five = 5] = [1, 2, 3, 4];

var a = "foo";
var b = "bar";
[a, b] = [b, a]; // variable swap

/**
 * Objects
 */
const myKey = "idk";
const obj = {
  mushroom: "🍄",
  banana: "🍌",
  pepper: "🌶️",
  "cute-dog": "🐶",
  parent: {
    child: "👶",
  },
  [myKey]: "🤪",
};
const { pepper, banana } = obj;
const { mushroom: shroom, "cute-dog": cuteDog } = obj;
const {
  parent: { child },
} = obj;
const { [myKey]: myKey } = obj; // dynamic name (computed at runtime)

/**
 * Strings
 */
var str = "abc";
var [a, b, c] = str;

var str = "fee fi fo fum";
var [fee, fii, fo, fum] = str.match(/\w+\s/g);
