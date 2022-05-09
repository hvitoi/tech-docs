let a = "José`";
let b = "José";

console.log(a == b);
console.log(a.normalize("NFC") == b.normalize("NFC"));
