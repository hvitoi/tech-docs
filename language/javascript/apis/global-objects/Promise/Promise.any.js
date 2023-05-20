const promise1 = Promise.reject(0);
const promise2 = new Promise((resolve) => setTimeout(resolve, 100, "quick"));
const promise3 = new Promise((resolve) => setTimeout(resolve, 500, "slow"));

// Return the first resolved promise
// Similar to Promise.race, the difference is that rejected promises are ignored
Promise.any([promise1, promise2, promise3]).then((value) => console.log(value));
// expected output: "quick"
