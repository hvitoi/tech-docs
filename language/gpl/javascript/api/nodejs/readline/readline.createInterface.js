const readline = require("node:readline");

var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

rl.on("line", (line) => {
  if (line === "stop") {
    rl.close()
    return
  }
  console.log(line);
});

rl.on('close', () => {
  console.log("I'm closing!")
});
