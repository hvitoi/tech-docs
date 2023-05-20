const crypto = require("crypto");

const algorithm = "sha256";
const data = "I love cupcakes";

// Hash the text and digests (outputs) as hexadecimal
const hash = crypto.createHash(algorithm).update(data).digest("hex");

console.log(hash);
