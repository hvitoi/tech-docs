const factorial = (n) => {
  // return [...Array(n).keys()]
  //   .map((el) => el + 1)
  //   .reduce((prod, el) => (prod *= el), 1);
  return Array.from({ length: n }, (_, i) => i + 1).reduce(
    (prod, el) => (prod *= el),
    1
  );
};

const factorial2 = (n) => {
  if (n === 0) return 1;
  return n * factorial2(n - 1);
};

// Proper Tail calls (PTC) optimization - prevent stack overflow errors
const factorial3 = (n, product = 1) => {
  if (n === 0) return product;
  return factorial3(n - 1, product * n); // no leftover processing required
};

console.log(factorial(10465)); // Infinity
// console.log(factorial2(10465)); // stackoverflow
// console.log(factorial3(10465));
