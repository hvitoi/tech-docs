main() {
  final name; // type inference (in this case will be "dynamic")
  final String name2; // type annotation (explicit)

  // a final variable can be assigned a value only once (at runtime)
  name = "Greg";

  // if trying to assign again it will fail
  // name = "John"; // fail!
}
