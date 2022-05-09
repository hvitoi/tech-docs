const buffer1 = Buffer.from("abc");
const buffer2 = Buffer.from("def");

const joinedBuffer = Buffer.concat([buffer1, buffer2]);

console.log(joinedBuffer.toString("utf8"));
