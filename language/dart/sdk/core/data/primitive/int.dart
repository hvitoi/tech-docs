void main() {
  // Static
  intNew();
  intTryParse();
}

void intNew() {
  int myInt = 29; // type explicit
  var myVar = 29; // type inference

  num myNum = 29; // parent class
}

void intTryParse() {
  int? parsed = int.tryParse("123");
}
