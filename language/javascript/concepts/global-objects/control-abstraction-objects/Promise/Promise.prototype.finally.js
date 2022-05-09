const myPromise = new Promise((resolve, reject) => {
  resolve("Resolved!");
});

myPromise
  .then((result) => {
    console.log("Success!", result);
  })
  .finally(() => {
    console.log("I will be executed anyway");
  });
