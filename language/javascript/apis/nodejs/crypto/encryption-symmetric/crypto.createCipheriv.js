const crypto = require("crypto");

const algorithm = "aes256";
const key = crypto.randomBytes(32);
const iv = crypto.randomBytes(16); // Initial Vector: prevent identical sequences of text
const data = "I love cupcakes";

// Encrypt
const cipher = crypto.createCipheriv(algorithm, key, iv);
const encrypted = Buffer.concat([cipher.update(data), cipher.final()]);
// const encrypted = cipher.update(data, "utf8", "hex") + cipher.final("hex");

// Decrypt
const decipher = crypto.createDecipheriv(algorithm, key, iv);
const decrypted = Buffer.concat([decipher.update(encrypted), decipher.final()]);
// const decrypted = decipher.update(encrypted, "hex", "utf8") + decipher.final("utf8");

// Results
console.log(encrypted.toString("hex"));
console.log(decrypted.toString("utf8"));
