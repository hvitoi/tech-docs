var start = Date.now();

// task starts
for (var i = 0; i < 100000000; i++);
// task ends

var end = Date.now();
console.log(`Execution time: ${end - start} ms`);
