void main() {
  /**
   * Static
   */
  doubleNew();

  doubleParse();
  doubleTryParse();
  doubleInfinity(); // property

  /**
   * Instance
   */
  doubleToString();
  doubleToStringAsFixed();
}

double doubleNew() {
  double d1 = 29.99;
  num d2 = 29.99; // parent class

  return d1;
}

void doubleParse() {
  double parsed = double.parse("176.28");
}

void doubleTryParse() {
  // null if not parsed
  double? parsed = double.tryParse("176.28");
}

void doubleInfinity() {
  double infinity = double.infinity;
}

void doubleToString() {
  double d1 = doubleNew();
  d1.toString();
}

void doubleToStringAsFixed() {
  double d1 = doubleNew();
  d1.toStringAsFixed(4); // 4 decimals rounded
}
