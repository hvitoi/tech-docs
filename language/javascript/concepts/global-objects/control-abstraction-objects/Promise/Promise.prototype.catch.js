const myPromise = new Promise((resolve, reject) => {
  reject("Rejected!");
});

myPromise.catch((result) => {
  console.log("Fail!", result);
});
