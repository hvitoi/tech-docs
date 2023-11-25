const myPromise = new Promise((resolve) => resolve("Resolved!"));

myPromise.then((result) => {
  console.log("Success!", result);
});

/**
 * Chained Promises
 */

const add = (a, b) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(a + b);
    }, 1000);
  });
};

add(1, 1)
  .then(
    // handle resolved
    (sum) => {
      console.log(sum);
      return add(sum, 1);
    },
    // handle rejected
    (e) => {}
  )
  .then(
    // handle resolved
    (sum2) => {
      console.log(sum2);
      return add(sum2, 1);
    },
    // handle rejected
    (e) => {}
  )
  .then(
    // handle resolved
    (sum3) => {
      console.log(sum3);
    },
    // handle rejected
    (e) => {}
  )
  .catch((err) => {
    console.log(err);
  });
