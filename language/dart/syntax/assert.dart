main() {
  // asserts are commonly used as a "guard clausule" in constructors in order
  // the validate the arguments passed to initialize a new object
  // all assert codes are ignored in production
  assert(0 == 1 || (throw "a"));
}
