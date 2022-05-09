process.stdin.resume();
process.stdin.setEncoding("ascii");

const textInput = [];

process.stdin.on("data", (line) => {
  textInput.push(line);
});

process.stdin.on("end", () => {
  for (let i = 1; i <= textInput[0]; i++) {
    if (!textInput[i]) break;
    const numbers = textInput[i]
      // .trim()
      .split(" ")
      .map((el) => parseInt(el));
    const sum = numbers.reduce((sum, el) => sum + el, 0);
    process.stdout.write("\n" + sum.toString());
  }
});
