const arr = [1, 2, 3, 4, 5];

for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]);
  if (arr[i] == 2) break; // Stops the for loop after printing 'Money'
}

for (let i = 0; i < arr.length; i++) {
  if (arr[i] == 2) continue; // Skip printing 'Money' and continues the loop
  console.log(arr[i]);
}
