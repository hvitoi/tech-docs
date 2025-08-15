main() {
  // a const variable must have its value assigned at declaration at compilation
  // a const variable is implicitly also final, because it can't be reassigned
  const name = "Henry"; // type inference
  const String name2 = "Henry"; // type annotation (explicit)

  // name = "Greg"; // fail!
}
