const crypto = require("crypto");

const { privateKey, publicKey } = crypto.generateKeyPairSync("rsa", {
  modulusLength: 2048, // length of the key in bits
  publicKeyEncoding: {
    type: "spki", // recommended by nodejs doc
    format: "pem", // Privacy Enhanced Mail (PEM) - based64 encoded
  },
  privateKeyEncoding: {
    type: "pkcs8", // recommended by nodejs doc
    format: "pem", // Privacy Enhanced Mail (PEM) - based64 encoded
    // cipher: "aes-256-cbs",
    // password: "top-secret",
  },
});

console.log(publicKey); // used for encryption
console.log(privateKey); // used for decryption
