const set = new Set(["b", "c", "a"]);

set.forEach((el) => console.log(el));

// ---

const areSetsEqual = (s1, s2) => {
  if (s1.size !== s2.size) return false;
  for (let item of s1) {
    if (!s2.has(item)) return false;
  }
  return true;
};
console.log(areSetsEqual(new Set(["a", "b"]), new Set(["b", "a"]))); // true
