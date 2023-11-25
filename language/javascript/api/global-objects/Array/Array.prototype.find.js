// O(N)

const arr = ["a", "b", "c", "d", "b"];

// Returns the first element that matches the criteria
const found = arr.find((el) => el === "b");
console.log(found);

// Returns undefined if not found
const notFound = arr.find((el) => el === "f");
console.log(notFound);
