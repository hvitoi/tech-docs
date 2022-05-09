const crypto = require("crypto");

const { privateKey, publicKey } = crypto.generateKeyPairSync("rsa", {
  modulusLength: 2048,
  publicKeyEncoding: { type: "spki", format: "pem" },
  privateKeyEncoding: { type: "pkcs8", format: "pem" },
});

// ---

const data = Buffer.from("the british are coming!");

// Sign
const signer = crypto.createSign("rsa-sha256"); // RSA + SHA
const dataSigned = signer.update(data).sign(privateKey, "hex");

// Verify
const verifier = crypto.createVerify("rsa-sha256");
const isVerified = verifier.update(data).verify(publicKey, dataSigned, "hex");

console.log(dataSigned);
console.log(isVerified);
