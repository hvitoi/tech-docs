const { Buffer } = require('node:buffer');

const text = "abc";
const buffer = Buffer.from(text);

console.log(buffer.toString("base64"));
