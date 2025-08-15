const number = "999";
const notNumber = "t999";

// Convert the price into float number
const numberFloat = parseFloat(number);
const notNumberFloat = parseFloat(notNumber);
console.log(numberFloat);
console.log(notNumberFloat);

// NaN if the price value is Not A Number
if (isNaN(numberFloat)) {
  console.log(`'${numberFloat}' is not a number`);
}
if (isNaN(notNumberFloat)) {
  console.log(`'${notNumberFloat}' is not a number`);
}
