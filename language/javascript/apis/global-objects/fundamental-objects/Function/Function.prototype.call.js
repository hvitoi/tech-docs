const myFn = (text) => console.log(text);

// same as apply(), the difference is that args are passed as individual elements (not array)
myFn.apply(null, "oi", "haha");
myFn.apply(null, ...["oi", "haha"]);
