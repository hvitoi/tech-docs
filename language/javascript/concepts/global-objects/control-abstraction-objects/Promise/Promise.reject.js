// returns a Promise object that is rejected with a given reason

Promise.reject(new Error("fail")).then(
  (res) => console.log(res),
  (res) => console.error(res) // this one will be executed
);
