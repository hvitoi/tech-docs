const fs = require("fs");

const obj = {
  a: 1,
  b: 2,
};

const data = JSON.stringify(obj);
fs.writeFileSync("notes.json", data);
