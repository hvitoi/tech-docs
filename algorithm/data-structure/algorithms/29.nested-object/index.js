const myObj = {
  a: "1",
  b: 2,
  c: {
    d: 3,
    e: {
      f: 4,
      g: 5,
    },
    h: 6,
  },
};

const printValues = (obj) => {
  if (typeof obj !== "object") {
    console.log(obj); // if there is no nested obj, print value
    return;
  }

  for (let key in obj) {
    printValues(obj[key]); // if there is nested obj, call printObj
  }
};

const printKeysAndValues = (obj) => {
  for (let key in obj) {
    if (typeof obj[key] === "object") {
      printKeysAndValues(obj[key]);
    } else {
      console.log(key + ":" + obj[key]);
    }
  }
};

const printKeysAndValuesWithSpacing = (obj, level = 0) => {
  for (let key in obj) {
    if (typeof obj[key] === "object") {
      printKeysAndValuesWithSpacing(obj[key], level + 1);
    } else {
      const spacing = "  ".repeat(level);
      console.log(spacing + key + ":" + obj[key]);
    }
  }
};

function printKeysAndValuesWithSpacing2(obj, level = 0) {
  Object.entries(obj).map(([key, value]) => {
    const spacing = " ".repeat(level);
    if (typeof value === "object") {
      console.log(`${spacing}${key} {`);
      printKeysAndValuesWithSpacing2(value, level + 1);
      console.log(`${spacing}}`);
    } else {
      console.log(`${spacing}${key}: ${value}`);
    }
  });
}

printValues(myObj);
console.log("-----");
printKeysAndValues(myObj);
console.log("-----");
printKeysAndValuesWithSpacing(myObj);
console.log("-----");
printKeysAndValuesWithSpacing2(myObj);
