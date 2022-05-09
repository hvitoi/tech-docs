void main() {
  bool condition = (1 == 1 && 2 > 1 && 1 < 2) || 1 != 1;

  // if-else
  if (condition) {
    print("true");
  } else if (condition) {
    // ...
  } else {
    print("false");
  }

  // ternary
  condition ? print("true") : print("false");
}
