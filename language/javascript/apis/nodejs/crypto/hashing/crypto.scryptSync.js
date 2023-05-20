const crypto = require("crypto");

const data = "I love cupcakes";
const salt = crypto.randomBytes(16);
const length = 40;

// Hash with salt
const hash = crypto.scryptSync(data, salt, length);
console.log(hash.toString("hex"));

/**
 * Usually the hashed data is stored along with its salt in the database
 * ${salt}:${hashedDataWithSalt}
 */
