const promise1 = Promise.resolve("promise1");
const promise2 = Promise.reject("promise2");
const promise3 = "promise3";
const promise4 = new Promise((resolve) => setTimeout(resolve, 100, "promise4"));

// "then" is executed when and if all promises are resolved
// "catch" is executed if any promise is rejected
Promise.all([promise1, promise2, promise3, promise4])
  .then((res) => {
    console.log(res); // array with the results from each resolved promise
  })
  .catch((res) => {
    console.log(res); // result of the first rejected promise
  });

//
(async () => {
  // same as promise.all: wait the array of promises to resolve concurrently and loop over it after all promises have been resolved
  for await (const res of [promise1, promise2, promise3, promise4]) {
    console.log(res);
  }
})();
