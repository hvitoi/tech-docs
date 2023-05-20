// Callback function is a function provided as an argument to another function

// Async Callback
setTimeout(() => {
  console.log("2 seconds");
}, 2000);

// Sync Callback
const names = ["Joao", "Maria", "Jose"];
// Here the callback function is used. But it is not interating with the node API
const shortNames = names.filter((name) => name.length <= 4); // Filter names with 4 or less words
console.log(shortNames);

// --------------------

// Creating functions to take callback functions
const geocode = (address, callback) => {
  setTimeout(() => {
    const data = {
      latitude: 0,
      longitude: 0,
    };
    callback(data);
  }, 2000);
};

geocode("Philadelphia", (data) => {
  console.log(data);
});

// --------------------

const add = (a, b, callback) => {
  setTimeout(() => {
    callback(a + b);
  }, 2000);
};

add(1, 4, (sum) => {
  console.log(sum); // Should print: 5
});
