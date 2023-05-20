process.stdin.resume();
process.stdin.setEncoding("utf-8");

let input = "";

process.stdin.on("data", (line) => {
  input += line;
});

process.stdin.on("end", () => {
  process.stdout.write(input);
});
