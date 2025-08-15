main() {
  var foo = 1;

  // fallback mechanism
  // sets a default value if foo is null
  var map = {'a': foo ?? ''};
}
