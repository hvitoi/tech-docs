const crypto = require("crypto");

const random = crypto.randomBytes(4);

console.log(random); // Buffer
console.log(random.toString("hex"));
console.log(random.toString("utf8"));
console.log(random.toString("base64"));
console.log(random.toString("binary"));
