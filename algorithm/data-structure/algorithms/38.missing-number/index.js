const arr = [1, 2, 3, 4, 6, 7, 8]; // 5 is missing

const n = arr.length + 1;
const fullSize = (n * (n + 1)) / 2;

const arrSize = arr.reduce((sum, el) => sum + el);

console.log(fullSize - arrSize);

// --

for (let i = 0; i < arr.length; i++) {
  if (i + 1 !== arr[i]) {
    console.log(i + 1);
    break;
  }
}
