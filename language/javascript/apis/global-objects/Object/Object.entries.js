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

const printNested2 = (obj, level = 0) => {
  Object.entries(obj).map(([key, value]) => {
    const spacing = " ".repeat(level);
    if (typeof value === "object") {
      console.log(`${spacing}${key} {`);
      printNested2(value, level + 1);
      console.log(`${spacing}}`);
    } else {
      console.log(`${spacing}${key}: ${value}`);
    }
  });
};

const printNested = (obj, level = 0) => {
  const spacing = " ".repeat(level);
  console.log(spacing + "{");
  // percorrer cada key-value do obj
  Object.entries(obj).forEach(([key, value]) => {
    // verificar se value é um novo objeto
    if (typeof value !== "object") {
      // se nao -> print
      console.log(`${spacing}${key}: ${value}`);
    } else {
      // se sim -> recursao
      console.log(`${spacing}${key}: `);
      printNested(value, level + 1);
    }
  });
  console.log(spacing + "}");
};

printNested(myObj);

// ---

// Take the key:value pair of each element and put in an array
const entries = Object.entries(myObj);
console.log(entries);
