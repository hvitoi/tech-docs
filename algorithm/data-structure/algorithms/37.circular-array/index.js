const arr = [0, 1, 2, 3, 4, 5];

const iter = 12;

for (let i = 0; i < iter; i++) {
  const idx = i % arr.length;
  console.log(arr[idx]);
}
