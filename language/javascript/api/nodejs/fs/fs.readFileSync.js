const fs = require("node:fs");

const dataBuffer = fs.readFileSync("notes.json");
const dataParsed = JSON.parse(dataBuffer.toString());

console.log(dataParsed);
