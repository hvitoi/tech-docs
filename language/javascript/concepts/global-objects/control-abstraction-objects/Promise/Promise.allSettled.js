const promise1 = Promise.reject("promise1");
const promise2 = new Promise((resolve) =>
  setTimeout(resolve, 1000, "promise2")
);

// Show if each promise has "fulfilled" or "rejected"
// The status is shown only has all of them have been executed completely
Promise.allSettled([promise1, promise2]).then((results) =>
  console.log(results)
);

// [
//   { status: 'rejected', reason: 'promise1' },
//   { status: 'fulfilled', value: undefined }
// ]
