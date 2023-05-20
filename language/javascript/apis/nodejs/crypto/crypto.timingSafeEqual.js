const crypto = require("crypto");

const buffer1 = crypto.randomBytes(16);
const buffer2 = crypto.randomBytes(16);

// Compare two buffers with protection against brute force
const match = crypto.timingSafeEqual(buffer1, buffer2);
console.log(match);
