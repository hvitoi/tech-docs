const codeList = [
  ["apple", "apple"],
  ["banana", "anything", "banana"],
];

const shoppingCart = ["orange", "apple", "apple", "banana", "orange", "banana"];

// if arr2 is a subset of arr1, returns the first index of arr1, else returns -1
const indexOf = (arr1, arr2) => {
  const maxIndex = arr1.length - arr2.length;
  for (let i = 0; i <= maxIndex; i++) {
    let isSubset = true;
    for (let j = 0; j < arr2.length; j++) {
      if (arr2[j] !== "anything" && arr1[i + j] !== arr2[j]) {
        isSubset = false; // cancel and break for if a different element is found
        break;
      }
    }
    if (isSubset) return i;
  }
  return -1;
};

const foo = (codeList, shoppingCart) => {
  //let startIndex = 0;
  for (const group of codeList) {
    //shoppingCart = shoppingCart.slice(startIndex); // slice shopping cart starting from the startIndex (guarantees the ordering of the groups)
    const idx = indexOf(shoppingCart, group); // if "group" is contained in "shoppingCart" in sequence
    if (idx === -1) {
      return 0;
    } else {
      shoppingCart = shoppingCart.slice(idx + group.length); // narrow down the shoppingCart array for the next iteration
      //startIndex = idx + group.length;
    }
  }
  return 1;
};
console.log(foo(codeList, shoppingCart));

module.exports = foo;
