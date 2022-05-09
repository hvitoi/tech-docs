// returns a Promise object that is resolved with a given value

Promise.resolve("Success!").then(
  (res) => console.log(res), // this one will be executed
  (res) => console.error(res)
);
