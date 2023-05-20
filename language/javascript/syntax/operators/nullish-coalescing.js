const obj = {
  a: undefined || "hey!", // undefined, null, empty string (""), etc
  b: undefined ?? "hey!", // only undefined and null shorts circuit to the right side
};
