// O(N)

const tempCelsius = [0, 50, 100];
const toFahrenheit = (temp) => (temp * 9) / 5 + 32;

// Execute a function a function for every element in the array
const tempFahrenheit = tempCelsius.map(toFahrenheit);

console.log(tempCelsius);
console.log(tempFahrenheit);
