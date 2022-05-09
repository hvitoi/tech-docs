const crypto = require("crypto");

/**
 * HMAC: Hash-based Message Authentication Code
 * Apply hash algorithm for the data+key
 * Results in a single final hash
 */

const algorithm = "sha256";
const key = "super-secret";
const data = "I love cupcakes";

const hash = crypto.createHmac(algorithm, key).update(data).digest("hex");
console.log(hash);
