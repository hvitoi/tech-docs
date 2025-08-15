// Async-await allow use of code that look synchronous to perform asynchronous tasks!

const add = (a, b) => {
  // add with timeout simulates a db query
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (a < 0 || b < 0) reject("Numbers must be non-negative");
      resolve(a + b);
    }, 1000);
  });
};

// async returns the result as a Promise. (e.g., Promise { 'Henrique' })
const doWork = async () => {
  const sum = await add(1, 1); // await can receive only Promises!
  const sum2 = await add(sum, 1);
  const sum3 = await add(sum2, 1); // If any of the 'add' functions get rejected it goes to the catch function
  return sum3;
};

// 'then-catch' expression can be used since the function is now a Promise
doWork()
  .then((result) => {
    console.log(result);
  })
  .catch((err) => {
    console.log(err);
  });

/**
 *
 *
 *
 *
 */
const returnHaha = new Promise((resolve) => {
  setTimeout(() => {
    resolve("haha");
  }, 1000);
});
const returnHehe = new Promise((resolve) => {
  setTimeout(() => {
    resolve("hehe");
  }, 1000);
});
const returnHihi = new Promise((resolve) => {
  setTimeout(() => {
    resolve("hihi");
  }, 1000);
});
const laughPromises = [returnHaha, returnHehe, returnHihi];

// ---

const findHehe = async () => {
  let myLaugh;
  for (let laughPromise of laughPromises) {
    const res = await laughPromise;
    if (res === "hehe") {
      myLaugh = res;
      break;
    }
  }
  if (myLaugh) {
    return myLaugh;
  } else {
    return await laughPromises[0];
  }
};

// ---

(async () => console.log(await findHehe()))();
