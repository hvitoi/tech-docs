// The Promise object represents the eventual completion (or failure) of an asynchronous operation and its resulting value.

// A Promise is in one of these states:
//     pending: initial state, neither fulfilled nor rejected.
//     fulfilled: meaning that the operation was completed successfully.
//     rejected: meaning that the operation failed.

const myPromise = new Promise((resolve, reject) => {
  // the first "resolve" or "reject" completed will be executed
  setTimeout(reject, 100000, "rejected in 100s");
  setTimeout(reject, 200000, "rejected in 200s");
  setTimeout(resolve, 5000, "resolved in 5s"); // first to complete (therefore the whole promise is resolved)
});

setTimeout(async () => {
  console.log(myPromise); // even though it has been resolved, it's still a promise
  console.log(await myPromise); // to extract the value of a promise you should use "await"
}, 6000);
