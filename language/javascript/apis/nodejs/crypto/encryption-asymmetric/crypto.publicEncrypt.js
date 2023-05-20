const crypto = require("crypto");

const { privateKey, publicKey } = crypto.generateKeyPairSync("rsa", {
  modulusLength: 2048,
  publicKeyEncoding: { type: "spki", format: "pem" },
  privateKeyEncoding: { type: "pkcs8", format: "pem" },
});

// ---

const data = Buffer.from("the british are coming!");

// Encrypt (private key)
const encryptedData = crypto.publicEncrypt(publicKey, data);

// Decrypt (public key)
const decryptedData = crypto.privateDecrypt(privateKey, encryptedData);

console.log(encryptedData.toString("hex"));
console.log(decryptedData.toString("utf8"));
