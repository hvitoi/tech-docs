// Run code after a time has passed. setTimeout(fn, t)
setTimeout(() => {
  console.log("2 seconds timer");
}, 2000);

// This function is executed at the end. The Call Stack executes the main function first!
setTimeout(() => {
  console.log("0 second timer");
}, 0);

console.log(
  "I get executed before anything, before I don't go to the event loop"
);
